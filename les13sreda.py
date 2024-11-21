import pandas as pd  # Импорт библиотеки для работы с данными
import numpy as np  # Импорт библиотеки для числовых операций
import matplotlib.pyplot as plt  # Импорт библиотеки для построения графиков
import seaborn as sns  # Импорт библиотеки для создания статистических графиков

file_path = "train.csv"  # Указываем путь к CSV файлу

# Источник активации виртуального окружения и установка необходимых библиотек:
# source venv/bin/activate
# pip install matplotlib

data = pd.read_csv(file_path) # Загружаем данные из CSV файла в DataFrame
# print(data.head(10))# Выводим первые 10 строк данных для ознакомления
# print(data.dtypes)# Выводим типы данных для каждого столбца в DataFrame
desc_stat = data.describe()# Получаем описательную статистику для всех числовых столбцов
desc_Gender = data["Gender"].value_counts()

data.drop(columns=["Product_ID", "User_ID", ])

# plp.figure(figsize=(10, 6))  # Устанавливаем размер графика # Визуализация статистики с помощью тепловой карты
# sns.heatmap(desc_stat, annot=True, cmap="YlGnBu", fmt=".2f")  # Строим тепловую карту
# plp.title("naznanie_pervonachalniye")  # Заголовок графика
# plp.show()

male = desc_Gender.get("M" , 0)
female = desc_Gender.get("F" , 0)

plt.bar(desc_Gender.index, desc_Gender.values)
plt.xlabel(f"M:{male}, F:{female}")
plt.title('Count of Men and Women')
plt.xticks(["F", "M"], ['Women', 'Men'])

mpocupki = data[data["Gender"] == "M"]["Purchase"]
fpocupki = data[data["Gender"] == "F"]["Purchase"]

plt.hist(mpocupki, bins=1, alpha=1, label='M', color='blue')
plt.hist(fpocupki, bins=1, alpha=1, label='F', color='orange')

plt.show()