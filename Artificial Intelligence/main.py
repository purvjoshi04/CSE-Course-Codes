import pandas as pd
import numpy as np
import os


csv_file_path = os.getenv('CSV_FILE_PATH')
if csv_file_path is None:
    print("Error: CSV file path is not provided in the environment variables.")
    exit()

try:
    data_frame = pd.read_csv(csv_file_path)
except FileNotFoundError:
    print("Error: CSV file not found. Please provide a valid file path.")
    exit()


x = np.array(data_frame['year'])
y = np.array(data_frame['duration'])


if len(x) != len(y):
    print("Error: Number of data points in X and Y do not match.")
    exit()


x_mean = np.mean(x)
y_mean = np.mean(y)


numerator = 0
denominator = 0
for i in range(len(x)):
    numerator += (x[i] - x_mean) * (y[i] - y_mean)
    denominator += np.square((x[i] - x_mean))
B1 = numerator / denominator
B0 = y_mean - (B1 * x_mean)

def predict_y(x_value):
    return B0 + B1 * x_value


while True:
    user_x = input("Enter the value of x (numeric value): ")
    if not user_x.replace('.', '', 1).isdigit(): 
        print("Error: Please enter a numeric value for x.")
    else:
        break

user_x = float(user_x)
predicted_y = predict_y(user_x)
print(f"Predicted y value for x = {user_x}: {predicted_y}")

# Step 8: Calculate R-squared
def calculate_r_squared(y_true, y_predicted):
    ss_total = np.sum((y_true - np.mean(y_true)) ** 2)
    ss_residual = np.sum((y_true - y_predicted) ** 2)
    r_squared = 1 - (ss_residual / ss_total)
    return r_squared


predicted_y = predict_y(x)
r_squared = calculate_r_squared(y, predicted_y)

print(f"R-squared: {r_squared}")

