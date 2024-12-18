import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
import seaborn as sns

# Подключение к базе данных
connect = sqlite3.connect("bookbaza.db")
cursor = connect.cursor()

# Исправленный SQL-запрос
data = pd.read_sql_query(
    "SELECT Genre, Age, [Annual Income (k$)], [Spending Score (1-100)] \
    FROM popitka3", connect
)

connect.close()

# Настройка графиков
sns.set(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# Создаем когорты
bins = [0, 18, 25, 35, 42, 55, 120]
zagolovki_dlya_stolbcov = ["0-18", "19-25", "26-35", "36-42", "43-55", "56+"]
data['Age Group'] = pd.cut(data['Age'], bins=bins, labels=zagolovki_dlya_stolbcov, right=False)

# Группировка данных
age_group_spending = data.groupby('Age Group')['Spending Score (1-100)'].mean().reset_index()

# Подсчет людей в каждой возрастной группе
podscheti_ludey = data['Age Group'].value_counts()
podscheti_ludey.sort_index().plot(kind='bar', color='pink', ax=axes[0, 0])
axes[0, 0].set_title("Распределение по возрастным группам")


# График средней копупательной способности по возрасту:
sns.barplot(x='Age Group', y='Spending Score (1-100)', data=age_group_spending, ax=axes[1,0], palette='pastel')
axes[1,0].set_title("Average Spending Score by Age Group")
axes[1,0].set_ylabel("Spending Score (1-100)")


# Распределение по полу
desc_Gender = data["Genre"].value_counts()
axes[0, 1].bar(desc_Gender.index, desc_Gender.values, color=['blue', 'orange'])
axes[0, 1].set_title("Распределение по полу")


# Группировка данных по полу и вычисление среднего значения
gender_spending = data.groupby('Genre')['Spending Score (1-100)'].mean().reset_index()
gender_spending.columns = ['Genre', 'Spending Score (1-100)']

# Построение графика
sns.barplot(x="Genre", y='Spending Score (1-100)', data=gender_spending, ax=axes[1,1], palette='pastel')
axes[1,1].set_title("Average Spending Score by Gender")
axes[1,1].set_ylabel("Spending Score")
axes[1,1].set_xlabel("Gender")

plt.tight_layout()
plt.show()

