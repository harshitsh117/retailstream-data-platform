from random import choice, randint, uniform

import pandas as pd
from faker import Faker

from .constants import BRANDS, PRODUCT_CATALOG, SUPPLIERS


class ProductGenerator:
    """Generates realistic product master data."""

    def __init__(self, locale: str = "en_IN"):
        self.fake = Faker(locale)

    def generate(
        self,
        count: int,
        start_id: int = 200001,
    ) -> pd.DataFrame:
        """Generate product records."""

        products = []

        for i in range(count):
            category = choice(list(PRODUCT_CATALOG.keys()))

            sub_category = choice(
                list(PRODUCT_CATALOG[category].keys())
            )

            product_name = choice(
                PRODUCT_CATALOG[category][sub_category]
            )

            brand = choice(BRANDS[category])

            supplier = choice(SUPPLIERS)

            unit_price = self._generate_unit_price(category)

            cost_price = round(
                unit_price * uniform(0.55, 0.80),
                2,
            )

            stock_quantity = self._generate_stock(category)

            launch_date = self.fake.date_between(
                start_date="-5y",
                end_date="today",
            )

            products.append(
                {
                    "product_id": start_id + i,
                    "product_name": product_name,
                    "category": category,
                    "sub_category": sub_category,
                    "brand": brand,
                    "supplier": supplier,
                    "unit_price": unit_price,
                    "cost_price": cost_price,
                    "stock_quantity": stock_quantity,
                    "launch_date": launch_date,
                    "is_active": choice(
                        [True] * 9 + [False]
                    ),
                }
            )

        return pd.DataFrame(products)

    @staticmethod
    def _generate_unit_price(category: str) -> float:
        """Generate realistic selling price."""

        price_ranges = {
            "Electronics": (2000, 80000),
            "Home Appliances": (1500, 50000),
            "Fashion": (300, 8000),
            "Groceries": (20, 500),
            "Furniture": (3000, 60000),
        }

        minimum, maximum = price_ranges[category]

        return round(
            uniform(minimum, maximum),
            2,
        )

    @staticmethod
    def _generate_stock(category: str) -> int:
        """Generate stock based on category."""

        stock_ranges = {
            "Electronics": (20, 200),
            "Home Appliances": (10, 100),
            "Fashion": (100, 1000),
            "Groceries": (500, 3000),
            "Furniture": (5, 50),
        }

        minimum, maximum = stock_ranges[category]

        return randint(
            minimum,
            maximum,
        )