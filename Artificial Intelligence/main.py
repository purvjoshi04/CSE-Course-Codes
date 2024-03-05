# import tkinter as tk
# from tkinter import filedialog
# import pandas as pd

# def browse_file():
#     file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
#     if file_path:
#         df = pd.read_csv(file_path)
#         print("CSV file loaded successfully.")
        
#     else:
#         print("No file selected.")


# root = tk.Tk()
# root.title("CSV File Selector")
# e
# browse_button = tk.Button(root, text="Browse CSV File", command=browse_file)
# browse_button.pack()

# # Run the Tkinter event loop
# root.mainloop()


import pandas as pd
import numpy as np

data_frame = pd.read_csv('Artificial Intelligence\dataset.csv')
# print(data_frame.to_csv())

x = np.array(data_frame['year'])
y = np.array(data_frame['duration'])

x_mean = np.mean(x)
y_mean = np.mean(y)


# finding regression here
numenator = 0
denominator = 0
for i in range(len(x)) :
    numenator+=(x[i]-x_mean) * (y[i]-y_mean)
    denominator+=np.square((x[i]-x_mean))
B1 = numenator/denominator


B0 = y_mean -(B1*x_mean)

def predict_y(x_value):
    return B0 + B1 * x_value

user_x = input("Enter the value of x: ")

try:
    user_x = float(user_x)
    
    predicted_y = predict_y(user_x)
    print(f"Predicted y value for x={user_x}: {predicted_y}")
except ValueError:
    print("Invalid input. Please enter a valid number for x.")
