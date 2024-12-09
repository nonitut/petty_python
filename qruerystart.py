import sqlite3

# cursor.execute("""
#     CREATE TABLE book(
#     book_id INT PRIMARY KEY , 
#     title VARCHAR(50),
#     author VARCHAR(30),
#     price DECIMAL(8, 2),
#     amount INT
# );
# """)  - создаем таблицу и столбцы в ней # DECIMAL - float

connect = sqlite3.connect("bookbaza.db")  # batabaze 
cursor = connect.cursor()

# cursor.execute("""
#     INSERT INTO book (book_id, title , author, price, amount ) 
#     VALUES (1, 'Мастер и Маргарита', 'Булгаков М.А.', 670.99, 3 )

# """)

connect.commit() # для сохранения изменений

cursor.execute('''SELECT * FROM book''')
rows = cursor.fetchall()
for i in rows :
    print(i)

connect.close() # закрываем баззу данный и защищаем ее


