import pandas as pd
import sqlite3
import matplotlib.pyplot as plt  # Импорт библиотеки для построения графиков
import seaborn as sns  # Импорт библиотеки для создания статистических графиков
# from sqlalchemy import create_engine # для переноса данных из csv в bd


# csv_file_path = './Mall_Customers.csv' 
# data = pd.read_csv(csv_file_path)

# Создайте соединение с SQLite базой данных / Если база данных не существует, она будет создана
# engine = create_engine('sqlite:///bookbaza.db')
# data.to_sql('popitka3', con=engine, if_exists='replace', index=False) # Запишите данные из DataFrame в таблицу в базе данных

connect = sqlite3.connect("bookbaza.db")  # batabaze 
cursor = connect.cursor()


data = pd.read_sql_query(
    "SELECT Genre, Age,'Annual Income (k$)', 'Spending Score (1-100)' \
    FROM popitka3", connect 
    )  # data frame - для хранения данных "\" - перенос строки df - data frame

connect.close()
# закрываем bd

sns.set(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
# axes - массив область для рисования графика 

sns.countplot(x="Age", data=data , ax=axes [0,0]) # sns.countplot - для под счета данных
axes[ 0, 0 ].set_title("Age")

plt.tight_layout()
plt.show()
# в слеедущий раз - кагортный вывод данных 