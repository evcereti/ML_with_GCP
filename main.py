import tomli as tomllib
from src.ingest import read_data, validate_schema
import logging
from logging import getLogger

logging.basicConfig(level=logging.INFO, format="%(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

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


if __name__ == "__main__":
    config = load_config()

    data_path = config["tables"]["churn"]["path"]["raw_local"]
    required_columns = config["tables"]["churn"]["schema"]["required_columns"]

    logger.info(f"Starting pipeline")
    df = read_data(data_path)
    if validate_schema(df, required_columns):
        logger.info(f"Data preview:\n{df.head()}")
    else:
        logger.error("Data schema validation failed.")