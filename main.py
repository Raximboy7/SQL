import sqlite3


db = sqlite3.connect('lesson_1.db')

cursor = db.cursor()# yozish metodi ishga tushirish

# cursor.execute('''CREATE TABLE IF NOT EXISTS company(
#     copmany_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     company_name TEXT,
#     year TEXT
# )''')







# cursor.execute('''INSERT INTO company(company_name, year)
# VALUES ('BMW','1913-08-23')''')
# name = 'Mercades Benz'
# year = '1926-02-19'
#
# cursor.execute('''INSERT INTO company(company_name, year)
# VALUES (?, ?)''', (name, year)) #ineksiyaga qarshi


db.commit()
db.close()