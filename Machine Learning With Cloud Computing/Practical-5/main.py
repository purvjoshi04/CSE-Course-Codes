import numpy as np
from sklearn.model_selection import KFold
from sklearn.metrics import r2_score, mean_squared_error
from dotenv import load_dotenv
from os.path import exists
from os import getenv
from pandas import read_csv
from sklearn.linear_model import LinearRegression


def k_fold_cross_validation(df, x_var, y_var, model, k=5):
    X = df[[x_var]]
    y = df[y_var]
    kf = KFold(n_splits=k, shuffle=True)
    scores = []
    errors = []
    squared_errors = []

    for train_index, test_index in kf.split(X):
        X_train, X_test = X.iloc[train_index], X.iloc[test_index]
        y_train, y_test = y.iloc[train_index], y.iloc[test_index]

        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        score = r2_score(y_test, y_pred)
        mse = mean_squared_error(y_test, y_pred)
        scores.append(score)
        errors.append(np.abs(y_test - y_pred))
        squared_errors.append(np.square(y_test - y_pred))

    return scores, errors, squared_errors


def valid_env(dataset: str, x_var: str, y_var: str):
    if not exists(dataset):
        raise FileNotFoundError(f"Dataset {dataset} does not exist")
    if x_var is None or y_var is None:
        raise Exception(
            f"Dataset {dataset} does not contain variables {x_var} and {y_var}"
        )


def main():
    load_dotenv()

    try:
        dataset = getenv("DATASET")
        independent_var = getenv("X_INDEPENDENT_VAR")
        dependent_var = getenv("Y_DEPENDENT_VAR")

        valid_env(dataset, independent_var, dependent_var)

        df = read_csv(dataset)

        if not df.columns.__contains__(dependent_var) or not df.columns.__contains__(
            independent_var
        ):
            raise Exception(
                f"{dependent_var} and {independent_var} do not exist in {dataset}"
            )

        model = LinearRegression()
        scores, errors, squared_errors = k_fold_cross_validation(
            df, independent_var, dependent_var, model, k=5
        )

        print("Evaluation scores for each fold:", scores)
        print("Average score:", np.mean(scores))

        # Calculate average error and average squared error
        avg_error = np.mean(np.concatenate(errors))
        avg_squared_error = np.mean(np.concatenate(squared_errors))
        print("Average error:", avg_error)
        print("Average squared error (MSE):", avg_squared_error)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
