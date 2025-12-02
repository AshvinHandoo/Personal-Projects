import argparse
from pathlib import Path
import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from src.data_utils import load_csv, train_test_split_df
from src.features import add_basic_features
from src.models import get_rf_baseline, build_tf_ffn
from src.eval import regression_metrics, plot_pred_vs_true

def preprocess_and_split(path, target):
    df = load_csv(path)
    df = add_basic_features(df)
    X_train, X_test, y_train, y_test = train_test_split_df(df, target)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    return X_train, X_test, y_train, y_test, scaler

def run_train(args):
    data_path = args.data
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    X_train, X_test, y_train, y_test, scaler = preprocess_and_split(data_path, args.target)

    # sklearn baseline
    rf = get_rf_baseline(n_estimators=200)
    rf.fit(X_train, y_train)
    rf_preds = rf.predict(X_test)
    rf_metrics = regression_metrics(y_test, rf_preds)
    print("RF metrics:", rf_metrics)
    joblib.dump(rf, out_dir / "rf_baseline.joblib")
    joblib.dump(scaler, out_dir / "scaler.joblib")

    # TensorFlow model
    import tensorflow as tf
    tf_model = build_tf_ffn(X_train.shape[1])
    tf_model.fit(X_train, y_train, validation_split=0.1, epochs=10, batch_size=32, verbose=1)
    tf_preds = tf_model.predict(X_test).squeeze()
    tf_metrics = regression_metrics(y_test, tf_preds)
    print("TF metrics:", tf_metrics)
    tf_model.save(out_dir / "tf_model")

    # save metrics and plot
    import json
    metrics = {"rf": rf_metrics, "tf": tf_metrics}
    with open(out_dir / "metrics.json", "w") as f:
        json.dump(metrics, f, indent=2)

    plot_pred_vs_true(y_test, rf_preds, out_path=out_dir / "rf_pred_vs_true.png")
    plot_pred_vs_true(y_test, tf_preds, out_path=out_dir / "tf_pred_vs_true.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, required=True)
    parser.add_argument("--out_dir", type=str, default="results")
    parser.add_argument("--target", type=str, default="response")
    args = parser.parse_args()
    run_train(args)
