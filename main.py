from src.generate_data import generate_data
from src.transform import load_data
from src.train_model import train
from src.predict import predict
from src.visualization import plot_results
from src.llm_insights import generate_insights

import pandas as pd


def run_pipeline():
    print("Starting Smart Backyard Pipeline")

    # 1. Generate data
    print("Generating data...")
    generate_data()

    # 2. Load data
    print("Loading data...")
    df = load_data("data/raw/backyard_data.csv")

    # 3. Train model
    print("Training model...")
    model = train(df)
    print(model)

    # 4. Make predictions
    print("Making predictions...")
    df_predictions = predict(model, df)

    # 5. Save predictions
    print("Saving predictions...")
    df_predictions.to_csv("outputs/predictions.csv", index=False)

    # generate human-readable explanations
    generate_insights(df_predictions, output_file="outputs/insights.txt")
    
    # 6. Visualize
    print("Generating visualization...")
    plot_results(df_predictions)

    print("Pipeline complete!")


if __name__ == "__main__":
    run_pipeline()
