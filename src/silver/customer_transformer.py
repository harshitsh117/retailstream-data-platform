from __future__ import annotations

import re

import pandas as pd

from src.project_logging.logger import Logger
from src.silver.base_transformer import BaseTransformer


class CustomerTransformer(BaseTransformer):
    """
    Transforms customer data from Bronze to Silver.
    """

    EMAIL_PATTERN = re.compile(
        r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    def __init__(self) -> None:
        super().__init__()
        self.logger = Logger.get_logger(__name__)

    def transform(
        self,
        dataframe: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Apply customer-specific transformations.
        """

        self.logger.info("Starting Customer Transformation...")

        df = dataframe.copy()

        # ------------------------------------
        # Common Transformations
        # ------------------------------------

        df = self.remove_duplicates(df)

        df = self.trim_strings(df)

        df = self.convert_datetime(
            df,
            ["registration_date"],
        )

        # ------------------------------------
        # Standardize Names
        # ------------------------------------

        df["first_name"] = df["first_name"].str.title()

        df["last_name"] = df["last_name"].str.title()

        df["full_name"] = (
            df["first_name"] + " " + df["last_name"]
        )

        # ------------------------------------
        # Standardize Emails
        # ------------------------------------

        df["email"] = df["email"].str.lower()

        # ------------------------------------
        # Validate Email Format
        # ------------------------------------

        valid_email_mask = df["email"].apply(
            lambda value: bool(
                self.EMAIL_PATTERN.match(value)
            )
        )

        invalid_count = (~valid_email_mask).sum()

        if invalid_count > 0:
            self.logger.warning(
                "Dropping %d customers with invalid emails.",
                invalid_count,
            )

        df = df[valid_email_mask]

        # ------------------------------------
        # Ensure Unique Customer IDs
        # ------------------------------------

        df = df.drop_duplicates(
            subset=["customer_id"]
        )

        self.logger.info(
            "Customer Transformation Complete (%d records).",
            len(df),
        )

        return df.reset_index(drop=True)