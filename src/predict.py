def predict(model, df):
    X = df[["temperature", "humidity", "sunlight_hours"]]
    df["prediction"] = model.predict(X)
    return df
