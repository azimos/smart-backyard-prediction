import os
import pandas as pd
from openai import OpenAI

# Initialize client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_insights(df: pd.DataFrame, output_file="outputs/insights.txt"):
    insights = []

    for idx, row in df.iterrows():
        prompt = (
            f"Given the following environmental data:\n"
            f"Temperature: {row['temperature']}\n"
            f"Humidity: {row['humidity']}\n"
            f"Sunlight hours: {row['sunlight_hours']}\n"
            f"Soil moisture: {row['soil_moisture']}\n"
            f"Prediction (needs water): {row['needs_water']}\n\n"
            f"Explain in simple terms why the model made this prediction."
        )

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        text = response.choices[0].message.content.strip()
        insights.append(text)

    # Save to file
    with open(output_file, "w") as f:
        for line in insights:
            f.write(line + "\n\n")

    print(f"Generated {len(insights)} LLM insights and saved to {output_file}")
