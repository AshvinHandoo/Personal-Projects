import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

def regression_metrics(y_true, y_pred):
    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    return {"mse": float(mse), "r2": float(r2)}

def plot_pred_vs_true(y_true, y_pred, out_path=None):
    plt.figure(figsize=(5,5))
    plt.scatter(y_true, y_pred, alpha=0.6, s=10)
    mn = min(min(y_true), min(y_pred))
    mx = max(max(y_true), max(y_pred))
    plt.plot([mn, mx], [mn, mx], color="k", linewidth=1)
    plt.xlabel("True response")
    plt.ylabel("Predicted response")
    plt.title("Predicted vs True")
    plt.tight_layout()
    if out_path is not None:
        plt.savefig(out_path, dpi=150)
    return plt
