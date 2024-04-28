# d) Find out the mean, median, mode
# e) Find out Standard Deviation.

from dotenv import load_dotenv
from os import getenv, path
from pandas import read_csv
from os.path import exists


def valid_env(dataset: str, column: str):
    if not path.exists(dataset):
        raise FileNotFoundError(f"Dataset '{dataset}' does not exist")
    if column is None:
        raise Exception("Define column variable")


def main():
    load_dotenv()
    try:
        dataset = getenv("DATASET")
        column = getenv("COLUMN")
        valid_env(dataset, column)

        df = read_csv(dataset)

        if not df.__contains__(column):
            raise Exception(
                "Column which you have provided in env does not exist in the datset"
            )

        column_mean = df[column].mean()
        column_median = df[column].median()
        column_mode = df[column].mode()[0]
        column_std_devation = df[column].std()

        print(f"{column}'s mean is {column_mean}")
        print(f"{column}'s median is {column_median}")
        print(f"{column}'s mode is {column_mode}")
        print(f"{column}'s standard deviation is {column_std_devation}")

    except Exception as e:
        print("An error occurred:", e)


main()
