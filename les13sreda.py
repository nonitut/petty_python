import pandas as pd
import numpy as np
import matplotlib.pyplot as plp
import seaborn as sns
file_path = "train.csv"
# source venv/bin/activate
# pip install matplotlib

data = pd.read_csv(file_path)
print(data.head(10)) # вывели первые 10 строк
print(data.dtypes) # вывели типы данных

desc_stat = data.describe()
# print(desc_stat) # статистика по таблице(иногда выыдает толковое что то)

plp.figure(figsize=(10,6))
sns.heatmap(desc_stat, annot=True, cmap="YlGnBu", fmt=".2f")
plp.title("naznanie_pervonachalniye")

plp.show()