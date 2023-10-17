import pandas as pd
import matplotlib.pyplot as plt
import random

plt.rc("font", family="Microsoft JhengHei")  # 讓 plt 可以顯示中文

df = pd.read_csv("111_studentsc.csv", encoding="utf-8")
df.isnull().sum().sum()  # 檢查空值數量
print(df)
