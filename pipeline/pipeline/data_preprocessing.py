import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    # Apply cleaning steps: drop nulls, encode, etc.
    return df_cleaned
