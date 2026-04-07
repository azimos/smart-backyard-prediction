import pandas as pd
import numpy as np

def generate_data(days=60):
    np.random.seed(42)

    data = []

    for i in range(days):
        temp = np.random.uniform(15, 35)
        humidity = np.random.uniform(30, 90)
        sunlight = np.random.uniform(4, 12)

        # synthetic logic
        moisture = (
            0.5 * humidity
            - 0.3 * temp
            + np.random.normal(0, 5)
        )

        needs_water = 1 if moisture < 20 else 0

        data.append({
            "temperature": temp,
            "humidity": humidity,
            "sunlight_hours": sunlight,
            "soil_moisture": moisture,
            "needs_water": needs_water
        })

    df = pd.DataFrame(data)
    df.to_csv("data/raw/backyard_data.csv", index=False)

    print("Data generated")

if __name__ == "__main__":
    generate_data()
