import pandas as pd
from os import getenv, path
from dotenv import load_dotenv


def main():
    load_dotenv()
    csv_file = getenv("DATASET")

    if not path.exists(csv_file):
        print("CSV file does not exist")
        return

    # d) How to read file in pandas
    csv_data = pd.read_csv(csv_file)
    print(
        "*****************************Original Dataset*********************************"
    )
    print(csv_data)
    print(
        "******************************************************************************"
    )
    column_1 = getenv("COLUMN_1").split(",")
    column_2 = getenv("COLUMN_2").split(",")
    # e) How to create data frame
    print("***************************** Data Frame *********************************")
    df = pd.DataFrame(
        {
            "Name": [
                "Braund, Mr. Owen Harris",
                "Allen, Mr. William Henry",
                "Bonnell, Miss. Elizabeth",
            ],
            "Age": [22, 35, 58],
            "Sex": ["male", "male", "female"],
        }
    )
    print(df)
    print("***************************************************************************")
    # f) How to clean Data by using pandas
    # b) Cleaning Empty Cells
    for column in column_1:
        if csv_data[column].hasnans:
            csv_data[column].fillna(csv_data[column].median(), inplace=True)

    # c) Cleaning Wrong Format
    for column in column_2:
        csv_data[column] = pd.to_datetime(csv_data[column], format="mixed")

    # d) Cleaning Wrong Data
    for column in csv_data.index:
        if (csv_data.loc[column, column_1] > 60).any():
            csv_data.loc[column, column_1] = 60

    # e) Removing Duplicates.
    csv_data.drop_duplicates(inplace=True)
    print("***************************** New Dataset *********************************")
    print(csv_data.to_string())
    print("***************************************************************************")


main()
