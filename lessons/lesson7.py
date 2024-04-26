# SQL - язык структурированных запросов
# база данных -
# СУБД- система управления базами данных
# NOsql:SQL
# posgreSQL,mySQL, SQLite3-2

# import sqlite3
#
# # CRUD - create reed update delete
# db = sqlite3.connect('op36_3.db')
# cursor = db.cursor()
#
# cursor.execute('''CREATE TABLE IF NOT EXISTS user (
# lastname TEXT,
# age INTEGER,
# view INTEGER,
# bitday DATE
# )''')
#
# # CREATE - INSERT INTO
# # cursor.execute('''INSERT INTO user VALUES ("beka",49,5,'2003-87-99')''')
#
# # UPDATE-UPDATE
# cursor.execute('''UPDATE user SET age=99 WHERE rowid!=2 ''')
#
#
#
# # REED-SELECT,fech
# cursor.execute('''SELECT rowid,* FROM user''')
# a=cursor.fetchall()
# for i in a:
#     print(i)
#
#
# db.commit()
# db.close()


import sqlite3

db = sqlite3.connect('op36_3.db')
cursor = db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS user (
    lastname TEXT,
    age INTEGER,
    view INTEGER,
    bitday DATE
)''')

cursor.execute('''INSERT INTO user VALUES ("Иванов", 25, 3, '2000-01-01')''')
cursor.execute('''INSERT INTO user VALUES ("Петров", 30, 4, '1995-05-05')''')
cursor.execute('''INSERT INTO user VALUES ("Сидоров", 35, 5, '1990-10-10')''')

cursor.execute('''UPDATE user SET age=99 WHERE rowid!=2''')

cursor.execute('''SELECT rowid,* FROM user''')
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''DELETE FROM user WHERE rowid % 2 = 0''')

cursor.execute('''SELECT rowid,* FROM user''')
rows = cursor.fetchall()
print("\nПосле удаления записей с четным rowid:")
for row in rows:
    print(row)

db.commit()
db.close()
