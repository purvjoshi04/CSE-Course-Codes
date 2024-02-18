import pandas as pd
import matplotlib.pyplot as plt

#write pandas code for plotting for csv file using matplotlib and use different `kind`` methods 

df = pd.read_csv('Position_Salaries.csv')


df.plot(kind='scatter', x='Level', y='Salary')
df.plot(kind='hist', x='Level', y='Salary')
df.plot(kind='line', x='Level', y='Salary')
df.plot(kind='bar', x='Level', y='Salary')
df.plot(kind='pie', x='Level', y='Salary')
df.plot(kind='box', x='Level', y='Salary')

plt.title('Postion Salries of employee by level and Salary')
plt.show()




