from os import getenv
from os.path import exists
from dotenv import load_dotenv
from pandas import read_csv
from scipy.stats import linregress 

def valid_env(dataset: str, x_var: str, y_var: str):
    if not exists(dataset):
        raise FileNotFoundError(f'Dataset {dataset} does not exist')
    if x_var is None and y_var is None:
        raise Exception('Dataset {dataset} does not contain variable {x_var} and {y_var}')

def main():
    load_dotenv()

    try:
        dataset = getenv('DATASET')
        indepedent_var = getenv("X_INDEPENDENT_VAR")
        dependent_var = getenv("Y_DEPENDENT_VAR")

        valid_env(dataset, indepedent_var, dependent_var)

        df = read_csv(dataset)

        if not df.__contains__(dependent_var) or not df.__contains__(indepedent_var):
            raise Exception(f"{dependent_var} and {indepedent_var} does not exist in {dataset}")
        
        regression_stats = linregress(df[dependent_var], df[indepedent_var])
        print(df)
        print("*************************** Regression Stats ***************************")
        print(f"Total Observations: {df.shape[0]}")
        print(f"Slope: {regression_stats.slope}")
        print(f"Intercept: {regression_stats.intercept}")
        print(f"Standard Error: {regression_stats.stderr}")
        print(f"R Squared: {regression_stats.rvalue}")
        print("*****************************************************************************")


    except Exception  as e:
        print(f"An error occurred {e}")

main()