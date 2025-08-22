import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier, plot_tree

FILE_ID = "1pDUe-oXGh_mqAORcGKKYIBkemNUMDVtC"
GID = "0"  
xlsx_url = f"https://docs.google.com/spreadsheets/d/{FILE_ID}/export?format=xlsx"
df = pd.read_excel(xlsx_url, engine="openpyxl")  
print(df.head())
print(df.info())

X = df.drop(columns=["id", "burnout60"])
y = df["burnout60"]

from sklearn.preprocessing import LabelEncoder
for col in X.select_dtypes(include=["object"]).columns:
    X[col] = LabelEncoder().fit_transform(X[col].astype(str))

print(X.head())
print(X.info())

X = df.iloc[:, 0:-1]
y = df["burnout60"]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                    test_size=0.3, 
                                                    random_state=42)
print("train 데이터: ", X_train.shape)
print("test 데이터: ", X_test.shape)