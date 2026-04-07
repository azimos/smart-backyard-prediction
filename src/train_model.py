def train(df):
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier

    X = df[["temperature", "humidity", "sunlight_hours"]]
    y = df["needs_water"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    print("Model accuracy:", model.score(X_test, y_test))

    return model

if __name__ == "__main__":
    train()
