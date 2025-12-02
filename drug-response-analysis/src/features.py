import numpy as np
import pandas as pd

def add_basic_features(df):
    df = df.copy()
    # example feature: log drug concentration (if present)
    if "drug_conc" in df.columns:
        df["log_drug_conc"] = np.log1p(df["drug_conc"])
    # row-wise summary features for numeric columns
    num = df.select_dtypes(include=[np.number])
    df["row_mean"] = num.mean(axis=1)
    df["row_std"] = num.std(axis=1)
    return df
