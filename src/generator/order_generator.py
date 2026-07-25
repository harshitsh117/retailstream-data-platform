from __future__ import annotations

import random
from datetime import datetime, timedelta
from typing import Dict, List

import pandas as pd
from faker import Faker

from src.generator.reference_data.orders import (
    PAYMENT_MODES,
    ORDER_STATUSES,
    ORDER_STATUS_WEIGHTS,
    DISCOUNT_PERCENTAGES,
    DISCOUNT_WEIGHTS,
    TAX_PERCENT,
    MIN_ITEMS_PER_ORDER,
    MAX_ITEMS_PER_ORDER,
    MIN_QUANTITY_PER_PRODUCT,
    MAX_QUANTITY_PER_PRODUCT,
    MIN_SHIPPING_DAYS,
    MAX_SHIPPING_DAYS,
    MIN_DELIVERY_DAYS,
    MAX_DELIVERY_DAYS,
    RETURN_WINDOW_DAYS,
    ORDER_HISTORY_DAYS,
    START_ORDER_ID,
    START_ORDER_ITEM_ID,
)


from src.project_logging.logger import Logger


class OrderGenerator:
    """
    Generates realistic retail Orders and Order Items.

    Parameters
    ----------
    customers_df : pd.DataFrame
        Customer master data.

    products_df : pd.DataFrame
        Product master data.
    """

    def __init__(
        self,
        customers_df: pd.DataFrame,
        products_df: pd.DataFrame,
        locale: str = "en_IN",
    ) -> None:
        """
        Initialize the Order Generator.
        """

        # -----------------------------------------
        # Logger
        # -----------------------------------------
        self.logger = Logger.get_logger(__name__)

        # -----------------------------------------
        # Faker
        # -----------------------------------------
        self.fake = Faker(locale)

        # -----------------------------------------
        # Source Data
        # -----------------------------------------
        self.customers_df = customers_df.copy()
        self.products_df = products_df.copy()

        # -----------------------------------------
        # Cached Customer IDs
        # Faster than dataframe.sample()
        # -----------------------------------------
        self.customer_ids: List[str] = (
            self.customers_df["customer_id"]
            .tolist()
        )

        # -----------------------------------------
        # Cached Product Records
        # Used during random product selection
        # -----------------------------------------
        self.product_records: List[Dict] = (
            self.products_df.to_dict("records")
        )

        # -----------------------------------------
        # Running IDs
        # -----------------------------------------
        self.next_order_id = START_ORDER_ID
        self.next_order_item_id = START_ORDER_ITEM_ID

        # -----------------------------------------
        # Statistics
        # -----------------------------------------
        self.total_orders_generated = 0
        self.total_order_items_generated = 0

        self.logger.info(
            "OrderGenerator initialized "
            f"with {len(self.customer_ids)} customers "
            f"and {len(self.product_records)} products."
        )
    def _generate_order_date(self) -> datetime:
        """
        Generate a random order date within the configured
        order history period.

        Returns
        -------
        datetime
            Random order date.
        """

        today = datetime.now()

        random_days = random.randint(0, ORDER_HISTORY_DAYS)

        order_date = today - timedelta(days=random_days)

        return order_date

    def _generate_shipment_date(
        self,
        order_date: datetime,
        order_status: str
    ) -> datetime | None:
        """
        Generate shipment date based on order status.

        Parameters
        ----------
        order_date : datetime
            Date when order was placed.

        order_status : str
            Current order status.

        Returns
        -------
        datetime | None
            Shipment date if applicable, otherwise None.
        """

        # Orders that never get shipped
        if order_status in ("Cancelled", "Processing"):
            return None

        # Shipment usually happens within 1–3 days
        shipping_days = random.randint(1, 3)

        shipment_date = order_date + timedelta(days=shipping_days)

        return shipment_date
    
    def _generate_delivery_date(
        self,
        shipment_date: datetime | None,
        order_status: str,
    ) -> datetime | None:
        """
        Generate delivery date based on shipment date and order status.

        Parameters
        ----------
        shipment_date : datetime | None
            Date when the order was shipped.

        order_status : str
            Current order status.

        Returns
        -------
        datetime | None
            Delivery date if applicable, otherwise None.
        """

        # Cannot deliver if it was never shipped
        if shipment_date is None:
            return None

        # Order is still in transit
        if order_status == "Shipped":
            return None

        # Only Delivered and Returned orders have delivery dates
        if order_status not in ("Delivered", "Returned"):
            return None

        # Delivery takes 2–7 days after shipment
        delivery_days = random.randint(2, 7)

        delivery_date = shipment_date + timedelta(days=delivery_days)

        return delivery_date

    def _calculate_amounts(
        self,
        unit_price: float,
        quantity: int,
        discount_percent: int,
    ) -> dict:
        """
        Calculate all monetary values for an order item.

        Parameters
        ----------
        unit_price : float
            Price of one unit.

        quantity : int
            Number of units purchased.

        discount_percent : int
            Discount percentage applied.

        Returns
        -------
        dict
            Dictionary containing calculated amounts.
        """

        # ----------------------------------------
        # Subtotal
        # ----------------------------------------

        subtotal = unit_price * quantity

        # ----------------------------------------
        # Discount
        # ----------------------------------------

        discount_amount = (
            subtotal * discount_percent
        ) / 100

        # ----------------------------------------
        # Taxable Amount
        # ----------------------------------------

        taxable_amount = subtotal - discount_amount

        # ----------------------------------------
        # GST
        # ----------------------------------------

        tax_amount = (
            taxable_amount * TAX_PERCENT
        ) / 100

        # ----------------------------------------
        # Final Amount
        # ----------------------------------------

        grand_total = taxable_amount + tax_amount

        return {
            "subtotal": round(subtotal, 2),
            "discount_amount": round(discount_amount, 2),
            "taxable_amount": round(taxable_amount, 2),
            "tax_amount": round(tax_amount, 2),
            "grand_total": round(grand_total, 2),
        }
    
    def _generate_order(self) -> dict:
        """
        Generate a single order header.

        Returns
        -------
        dict
            Order header information.
        """

        # -----------------------------------------
        # Generate Primary Key
        # -----------------------------------------
        order_id = self.next_order_id
        self.next_order_id += 1

        # -----------------------------------------
        # Select Customer
        # -----------------------------------------
        customer_id = random.choice(self.customer_ids)

        # -----------------------------------------
        # Order Status
        # -----------------------------------------
        order_status = random.choices(
            ORDER_STATUSES,
            weights=ORDER_STATUS_WEIGHTS,
            k=1,
        )[0]

        # -----------------------------------------
        # Payment Mode
        # -----------------------------------------
        payment_mode = random.choice(PAYMENT_MODES)

        # -----------------------------------------
        # Dates
        # -----------------------------------------
        order_date = self._generate_order_date()

        shipment_date = self._generate_shipment_date(
            order_date,
            order_status,
        )

        delivery_date = self._generate_delivery_date(
            shipment_date,
            order_status,
        )

        # -----------------------------------------
        # Build Order Header
        # -----------------------------------------
        order = {
            "order_id": order_id,
            "customer_id": customer_id,
            "order_date": order_date,
            "order_status": order_status,
            "payment_mode": payment_mode,
            "shipment_date": shipment_date,
            "delivery_date": delivery_date,
        }

        return order
    
    def _generate_order_items(
        self,
        order: dict,
    ) -> tuple[list[dict], float]:
        """
        Generate order items for a single order.

        Parameters
        ----------
        order : dict
            Order header.

        Returns
        -------
        tuple
            (
                order_items,
                order_grand_total
            )
        """

        order_items = []

        order_total = 0.0

        # -----------------------------------------
        # Number of Products
        # -----------------------------------------

        number_of_products = random.randint(
            MIN_ITEMS_PER_ORDER,
            MAX_ITEMS_PER_ORDER,
        )

        # -----------------------------------------
        # Select Unique Products
        # -----------------------------------------

        selected_products = random.sample(
            self.product_records,
            number_of_products,
        )

        # -----------------------------------------
        # Generate Order Item
        # -----------------------------------------

        for product in selected_products:

            quantity = random.randint(
                MIN_QUANTITY_PER_PRODUCT,
                MAX_QUANTITY_PER_PRODUCT,
            )

            discount_percent = random.choices(
                DISCOUNT_PERCENTAGES,
                weights=DISCOUNT_WEIGHTS,
                k=1,
            )[0]

            amounts = self._calculate_amounts(
                unit_price=product["unit_price"],
                quantity=quantity,
                discount_percent=discount_percent,
            )

            order_item = {

                "order_item_id": self.next_order_item_id,

                "order_id": order["order_id"],

                "product_id": product["product_id"],

                "product_name": product["product_name"],

                "category": product["category"],

                "sub_category": product["sub_category"],

                "quantity": quantity,

                "unit_price": product["unit_price"],

                "discount_percent": discount_percent,

                "subtotal": amounts["subtotal"],

                "discount_amount": amounts["discount_amount"],

                "taxable_amount": amounts["taxable_amount"],

                "tax_percent": TAX_PERCENT,

                "tax_amount": amounts["tax_amount"],

                "grand_total": amounts["grand_total"],
            }

            order_items.append(order_item)

            order_total += amounts["grand_total"]

            self.next_order_item_id += 1

        return (
            order_items,
            round(order_total, 2),
        )
    
    def generate(
        self,
        order_count: int = 10000,
    ) -> tuple[pd.DataFrame, pd.DataFrame]:
        """
        Generate Orders and Order Items.

        Parameters
        ----------
        order_count : int
            Number of orders to generate.

        Returns
        -------
        tuple
            (
                orders_df,
                order_items_df
            )
        """

        self.logger.info(
            f"Generating {order_count} orders..."
        )

        order_headers = []

        order_line_items = []

        for _ in range(order_count):

            # ---------------------------------------
            # Generate Order Header
            # ---------------------------------------

            order = self._generate_order()

            # ---------------------------------------
            # Generate Order Items
            # ---------------------------------------

            items, grand_total = self._generate_order_items(
                order
            )

            # ---------------------------------------
            # Update Order Total
            # ---------------------------------------

            order["grand_total"] = grand_total

            # ---------------------------------------
            # Save Records
            # ---------------------------------------

            order_headers.append(order)

            order_line_items.extend(items)

            # ---------------------------------------
            # Statistics
            # ---------------------------------------

            self.total_orders_generated += 1

            self.total_order_items_generated += len(items)

        # -------------------------------------------
        # Convert to DataFrames
        # -------------------------------------------

        orders_df = pd.DataFrame(order_headers)

        order_items_df = pd.DataFrame(order_line_items)

        self.logger.info(
            f"Generated {len(orders_df)} orders "
            f"and {len(order_items_df)} order items."
        )

        return (
            orders_df,
            order_items_df,
        )