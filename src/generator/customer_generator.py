from datetime import date
from random import choice
from typing import List

import pandas as pd
from faker import Faker


class CustomerGenerator:
    """Generates realistic customer master data."""

    def __init__(self, locale: str = "en_IN"):
        self.fake = Faker(locale)

        self.loyalty_tiers: List[str] = [
            "Bronze",
            "Silver",
            "Gold",
            "Platinum",
        ]

    def generate(
        self,
        count: int,
        start_id: int = 100001,
    ) -> pd.DataFrame:
        """Generate customer records."""

        customers = []

        for i in range(count):
            first_name = self.fake.first_name()
            last_name = self.fake.last_name()

            dob = self.fake.date_of_birth(
                minimum_age=18,
                maximum_age=75,
            )

            registration_date = self.fake.date_between(
                start_date="-5y",
                end_date="today",
            )

            customers.append(
                {
                    "customer_id": start_id + i,
                    "first_name": first_name,
                    "last_name": last_name,
                    "full_name": f"{first_name} {last_name}",
                    "email": self.fake.email(),
                    "phone": self.fake.phone_number(),
                    "gender": choice(["Male", "Female"]),
                    "date_of_birth": dob,
                    "city": self.fake.city(),
                    "state": self.fake.state(),
                    "country": "India",
                    "registration_date": registration_date,
                    "loyalty_tier": choice(self.loyalty_tiers),
                    "is_active": choice([True, True, True, False]),
                }
            )

        return pd.DataFrame(customers)