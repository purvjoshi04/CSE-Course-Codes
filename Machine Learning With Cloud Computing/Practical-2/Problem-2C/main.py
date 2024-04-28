#c) Plotting of different types of charts by using csv file in Matplotlib

import matplotlib.pyplot as plt
from dotenv import load_dotenv
from os import getenv, path
import pandas


def line_plot(dataset: pandas.DataFrame, x_data: str, y_data: str):
    plt.xlabel(x_data)
    plt.ylabel(y_data)
    plt.plot(dataset[x_data], dataset[y_data])
    plt.show()


def bar_plot(dataset: pandas.DataFrame, x_data: str, y_data: str):
    plt.xlabel(x_data)
    plt.ylabel(y_data)
    plt.bar(dataset[x_data], dataset[y_data])
    plt.show()


def scatter_plot(
    dataset: pandas.DataFrame, x_data: str, y_data: str, x_color: str, y_color: str
):
    plt.xlabel(x_data)
    plt.ylabel(y_data)
    plt.scatter(dataset[x_data], dataset[y_data], color=x_color, label=x_data)
    plt.scatter(dataset[x_data], dataset[y_data], color=y_color, label=y_data)
    plt.legend()
    plt.show()


def pie_plot(dataset: pandas.DataFrame, x_data, y_data):
    plt.pie(dataset[y_data], labels=dataset[x_data], autopct="%1.1f%%")
    plt.show()


def histogram_plot(dataset: pandas.DataFrame, x_data: str, y_data: str):
    plt.xlabel(x_data)
    plt.ylabel(y_data)
    plt.hist(dataset[x_data], edgecolor="white")
    plt.show()


def valid_env(dataset: str, x_data: str, y_data: str):
    if not path.exists(dataset):
        raise FileNotFoundError(f"Dataset '{dataset}' does not exist")
    if x_data is None or y_data is None:
        raise Exception("Please define x_data and y_data variable")


def main():
    try:
        load_dotenv()
        dataset = getenv("DATASET")
        x_data = getenv("X_DATA")
        y_data = getenv("Y_DATA")
        plot_types = getenv("PLOT_TYPES")

        valid_env(dataset, x_data, y_data)

        df = pandas.read_csv(dataset)
        if "Line Plot" in plot_types:
            line_plot(df, x_data, y_data)
        if "Bar Plot" in plot_types:
            bar_plot(df, x_data, y_data)
        if "Scatter Plot" in plot_types:
            scatter_plot(df, x_data, y_data, x_color="black", y_color="red")
        if "Pie Plot" in plot_types:
            pie_plot(df, y_data, x_data)
        if "Histogram Plot" in plot_types:
            histogram_plot(df, x_data, y_data)
    except Exception as e:
        print("An error occurred:", e)


main()
