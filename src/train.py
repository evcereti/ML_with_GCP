import pandas as pd

def read_data(path: str) -> pd.DataFrame:
    """Reads data from a CSV file and returns a DataFrame.

    Args:
        path (str): The file path to the CSV file.

    Returns:
        pd.DataFrame: The DataFrame containing the data from the CSV file.
    """

    return pd.read_csv(path)

if __name__ == "__main__":
    df = read_data("C:\\learn_ml_gcp\\ML_with_GCP\\data\\raw.csv")
    print(df.head())