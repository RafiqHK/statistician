import pandas as pd

def read_excel_file(file):
    try:
        df = pd.read_excel(file)
        return df
    except Exception as e:
        raise ValueError(f"Error reading Excel file: {str(e)}")

def clean_data(df):
    df = df.dropna()  # Remove rows with missing values
    return df

def prepare_data(df, dependent_var, independent_vars):
    if dependent_var not in df.columns or any(var not in df.columns for var in independent_vars):
        raise ValueError("Dependent or independent variables are not in the dataframe.")
    
    X = df[independent_vars]
    y = df[dependent_var]
    return X, y