import pandas as pd

def encode_gender(df, column="Gender"):
    """
    Encode gender column: Male → 0, Female → 1
    """
    df[column] = df[column].map({"Male": 0, "Female": 1})
    return df

def scale_income(df, column="Income"):
    """
    Scale income to thousands (optional)
    """
    df[column] = df[column] / 1000
    return df
