# сигментация по городу и по штату 
# Пандас для работы с xlsx 

import pandas as pd
file_path = "orders_data.xlsx"

data = pd.read_excel(file_path)
# попросили прочитать файл [171 rows x 12 columns]
# print(data)

# .iloc - свойство 
# first_ten_rows = data.iloc[:10]
# print(first_ten_rows)

slovarcity = {}
hranitel = data.iloc

for index_row , row in enumerate(hranitel):  
    # print(hranitel [index_row, 0])                         
    city = (hranitel [index_row, 3])  
    money = hranitel [index_row, 8]
    money = money.replace("₹", "").strip()
    if city in slovarcity :
        slovarcity[city] += float(money)
    else: 
        slovarcity[city] = 0
        
print(slovarcity)
