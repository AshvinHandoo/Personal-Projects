import pandas as pd
import numpy as np

def load_csv(path):
    df = pd.read_csv(path)
    return df

def train_test_split_df(df, target, test_size=0.2, random_state=42):
    from sklearn.model_selection import train_test_split
    df = df.copy()
    df = df.dropna(subset=[target])
    X = df.drop(columns=[target])
    y = df[target].values
    # keep numeric features only for this pipeline
    X = X.select_dtypes(include=[np.number]).fillna(0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test
