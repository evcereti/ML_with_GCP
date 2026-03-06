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


def enforce_types(df: DataFrame, rules: dict) -> DataFrame:  
    cols_to_numeric = rules.get('force_float', [])
    for col in cols_to_numeric:
        df[col] = pd.to_numeric(df[col], errors='coerce')
        df[col] = df[col].fillna(0.0)
    return df


def validate_schema(df: DataFrame, schema_columns: dict) -> bool:
    """Validates the schema of the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to validate.

    Returns:
        bool: True if the schema is valid, False otherwise.
    """

    missing_columns = set(schema_columns.keys()) - set(df.columns)

    if missing_columns:
        logger.info(f"Missing Columns: {missing_columns}")
        return False
    
    for column, schema_type in schema_columns.items():
        logger.info(f"Validating type {column} : {schema_type}")
        if df[column].dtype != schema_type:
            logger.info(f"Invalid type for column: Should be {column}:{schema_type} but is {column}:{df[column].dtype}")
            return False
    
    return True


def drop_columns(df: DataFrame, required_columns: list) -> DataFrame:
    """Determines which columns to drop from the DataFrame.

    Args:
        df (DataFrame): The DataFrame to analyze.
        required_columns (list): The list of required columns to keep.

    Returns:
        DataFrame: The DataFrame with the specified columns dropped.
    """
    drop_cols = [col for col in df.columns if col not in required_columns]

    logger.info(f"Dropping columns: {drop_cols}")
    df = df.drop(columns=drop_cols)
    return df