import pandas as pd

def load_data(path="data/cleaned_tourism_data.csv"):
    """
    Load CSV data from the given path.
    Default path points to cleaned dataset in the repo.
    """
    return pd.read_csv(path)

def clean_data(df):
    """
    Apply cleaning steps: drop nulls, encode categorical variables, etc.
    Customize this based on your actual cleaning logic.
    """
    df_cleaned = df.copy()
    # Example cleaning logic:
    # df_cleaned.dropna(inplace=True)
    # df_cleaned = pd.get_dummies(df_cleaned, drop_first=True)
    return df_cleaned
