import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier, plot_tree

FILE_ID = "1pDUe-oXGh_mqAORcGKKYIBkemNUMDVtC"
GID = "0"  
xlsx_url = f"https://docs.google.com/spreadsheets/d/{FILE_ID}/export?format=xlsx"
df = pd.read_excel(xlsx_url, engine="openpyxl")  
print(df.head())
print(df.info())
