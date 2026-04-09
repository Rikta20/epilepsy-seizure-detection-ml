import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score

data = {
    "mean": [0.21, 0.85, 0.35, 0.92, 0.18, 0.76, 0.40, 0.88, 0.30, 0.95],
    "std":  [0.05, 0.20, 0.08, 0.25, 0.04, 0.18, 0.09, 0.22, 0.06, 0.27],
    "min":  [0.10, 0.50, 0.12, 0.55, 0.08, 0.48, 0.15, 0.60, 0.11, 0.58],
    "max":  [0.35, 1.20, 0.50, 1.30, 0.28, 1.10, 0.58, 1.25, 0.44, 1.40],
    "label": [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[["mean", "std", "min", "max"]]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = SVC(kernel="linear")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
