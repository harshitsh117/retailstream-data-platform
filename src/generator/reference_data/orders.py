"""
Business reference data for generating retail orders.
"""

# -------------------------------------------------------
# Payment Modes
# -------------------------------------------------------

PAYMENT_MODES = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash on Delivery",
    "Wallet",
]

# -------------------------------------------------------
# Order Statuses
# -------------------------------------------------------

ORDER_STATUSES = [
    "Delivered",
    "Shipped",
    "Processing",
    "Cancelled",
    "Returned",
]

# Probability weights corresponding to ORDER_STATUSES
# These should sum to 100.
ORDER_STATUS_WEIGHTS = [
    70,   # Delivered
    10,   # Shipped
    10,   # Processing
    5,    # Cancelled
    5,    # Returned
]

# -------------------------------------------------------
# Discount Percentages
# -------------------------------------------------------

DISCOUNT_PERCENTAGES = [
    0,
    5,
    10,
    15,
    20,
]

# Probability weights for discounts.
DISCOUNT_WEIGHTS = [
    50,   # 0%
    20,   # 5%
    15,   # 10%
    10,   # 15%
    5,    # 20%
]

# -------------------------------------------------------
# Tax Configuration
# -------------------------------------------------------

TAX_PERCENT = 18

# -------------------------------------------------------
# Quantity Rules
# -------------------------------------------------------

MIN_ITEMS_PER_ORDER = 1
MAX_ITEMS_PER_ORDER = 5

MIN_QUANTITY_PER_PRODUCT = 1
MAX_QUANTITY_PER_PRODUCT = 4

# -------------------------------------------------------
# Shipping Rules
# -------------------------------------------------------

MIN_SHIPPING_DAYS = 1
MAX_SHIPPING_DAYS = 3

MIN_DELIVERY_DAYS = 2
MAX_DELIVERY_DAYS = 7

RETURN_WINDOW_DAYS = 10

# -------------------------------------------------------
# Order Generation
# -------------------------------------------------------

ORDER_HISTORY_DAYS = 730        # Last 2 years

START_ORDER_ID = 500001
START_ORDER_ITEM_ID = 900001