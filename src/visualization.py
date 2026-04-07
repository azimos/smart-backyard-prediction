import plotly.express as px

def plot_results(df):
    fig = px.scatter(
        df,
        x="temperature",
        y="humidity",
        color="prediction",
        title="Watering Prediction"
    )

    fig.write_html("outputs/charts.html")
