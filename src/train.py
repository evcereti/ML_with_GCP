import pandas as pd
import logging
from logging import getLogger
import tomli as tomllib

logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")

logger = getLogger(__name__)

def load_config(config_path: str = "config.toml") -> dict:
    """Loads configuration from a TOML file.

    Args:
        config_path (str): The file path to the TOML configuration file.

    Returns:
        dict: The configuration dictionary.
    """
    with open(config_path, "rb") as f:
        config = tomllib.load(f)
    return config


def read_data(path: str) -> pd.DataFrame:
    """Reads data from a CSV file and returns a DataFrame.

    Args:
        path (str): The file path to the CSV file.

    Returns:
        pd.DataFrame: The DataFrame containing the data from the CSV file.
    """
    logger.info(f"Reading data from {path}")
    return pd.read_csv(path)

if __name__ == "__main__":
    config = load_config()

    data_path = config["paths"]["raw_local"]

    df = read_data(data_path)
    logger.info(f"Data preview:\n{df.head()}")