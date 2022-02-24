import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def visualization(df : pd.DataFrame):
    sns.set_style("whitegrid")
    sns.lineplot(
        data=df,
        x="date",
        y="value",
        hue="country_region"
    )

    plt.xticks(rotation=15)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Latam covid time series")
    plt.show()

def visualization_color (df : pd.DataFrame):
    sns.set_style("whitegrid")
    sns.barplot(
        data=df,
        x="value",
        y="country_region",
        palette=df.color
    )

    plt.xlabel("Value")
    plt.ylabel("Country Region")
    plt.title("Latam countries in a global context") # Grafico aprovechando los colores
    plt.show()

