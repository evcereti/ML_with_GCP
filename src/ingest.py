import pandas as pd
from logging import getLogger
from pandas import DataFrame


logger = getLogger(__name__)


def read_data(path: str) -> pd.DataFrame:
    """Reads data from a CSV file and returns a DataFrame.

    Args:
        path (str): The file path to the CSV file.

    Returns:
        pd.DataFrame: The DataFrame containing the data from the CSV file.
    """
    logger.info(f"Reading data from {path}")
    return pd.read_csv(path)


def validate_schema(df: pd.DataFrame, required_columns: list) -> bool:
    """Validates the schema of the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to validate.

    Returns:
        bool: True if the schema is valid, False otherwise.
    """

    missing_columns = set(required_columns) - set(df.columns)

    if missing_columns:
        return False
    return True
