from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training set shape:")
print("X_train:", X_train)
print("y_train:", y_train)
print("\nTesting set shape:")
print("X_test:", X_test)
print("y_test:", y_test)
