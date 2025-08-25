#%%
import pandas as pd
from pandas.plotting import scatter_matrix
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import shap
import pycaret
#%%
df_raw = pd.read_csv("C:/Users/user/Desktop/2PD_v1_0822.csv", encoding='CP949')

df_raw.info()

df = df_raw
#%%
cols = [
    "wstat4", "wstat6",
    "wwa1", "wwa2", "wwa3", "wwa4", "wwa5",
    "sleep1", "sleep2", "sleep3",
    "imte1", "imte2", "imte3", "imte4", "imte5",
    "wsituation12", "wsituation14"
]

# 변환 딕셔너리 (5점 척도 역코딩)
reverse_map = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}

# 여러 열에 적용
for col in cols:
    df_raw[col] = df_raw[col].map(reverse_map).fillna(df_raw[col])


#%%
print(df_raw.columns.tolist())
#%%
print(df_raw[cols].head())
#%%
df["wstat4"].head(10) 

#%%
df_raw["heal_abs1"] = np.where(df_raw["heal_abs1"] == 0, 0, 1)
#%%
print(df_raw["heal_abs1"].head())
#%%
df_raw["heal_abs1"].value_counts()
#%%

# 구간 (0~60, 61~120, 181 이상)
bins = [0, 60, 120, float("inf")]
labels = [1, 2, 3]

df_raw["ctime_group"] = pd.cut(df_raw["ctime"], bins=bins, labels=labels, right=True)
#%%
print(df_raw["ctime_group"].head())
#%%
df_raw["ctime_group"].value_counts()
#%%
