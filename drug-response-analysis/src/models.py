import tensorflow as tf
from sklearn.ensemble import RandomForestRegressor

def get_rf_baseline(n_estimators=200):
    return RandomForestRegressor(n_estimators=n_estimators, random_state=42, n_jobs=-1)

def build_tf_ffn(input_dim):
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(input_dim,)),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(1)
    ])
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    return model
