import pandas as pd
import logging
from logging import getLogger
import tomli as tomllib


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
