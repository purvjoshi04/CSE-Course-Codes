import pandas as pd
# write pandas code for read, Replace and Remove for csv file 


# read csv file
read_csv = pd.read_csv('Position_Salaries.csv')
# print(read_csv)

# replace value only for numbers which is NaN in csv file
replacement_value = 10
for column in read_csv.columns:
    if read_csv[column].isna().any():
        read_csv[column].fillna(replacement_value, inplace=True)

read_csv.dropna(inplace=True)
read_csv.to_csv('modified_file.csv', index=False)
