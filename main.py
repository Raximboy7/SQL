import sqlite3


db = sqlite3.connect('lesson_1.db')

cursor = db.cursor()# yozish metodi ishga tushirish

# cursor.execute('''CREATE TABLE IF NOT EXISTS company(
#     copmany_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     company_name TEXT,
#     year TEXT
# )''')

# MALUMOT QOSHISH

# cursor.execute('''INSERT INTO company(company_name, year)
# VALUES ('BMW','1913-08-23')''')

# name = 'Mercades Benz'
# year = '1926-02-19'
# cursor.execute('''INSERT INTO company(company_name, year)
# VALUES (?, ?)''', (name, year)) #ineksiyaga qarshi

#
# cursor.executemany('''INSERT INTO company(company_name, year)
# VALUES (?, ?)''',[('Ferrari','1929-03-4'),('lambarghini','1963-05-4')])


# BIR NECHTA BUYRUQLAR (ma'lumot qo'shishdan tashqari)

# cursor.executescript('''DROP TABLE IF EXISTS cars;
# CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     car TEXT,
#     motor TEXT,
#     copmany_id INTEGER REFERENCES company(copmany_id)
# )''')


# cursor.executemany('''INSERT INTO cars(car, motor, copmany_id)
# VALUES (?, ?, ?)''', [('BMW 17','Hybrid',1), ('S223', '5',2),
#                                        ('BMW X7', 'sport',1), ('AMG', '6', 2),
#                                         ('Urus', 'Hybrid', 4)])


# Ma'lumorni Ko'rish

# cursor.execute('''SELECT * FROM cars
# WHERE copmany_id=(SELECT copmany_id FROM company WHERE company_name=?)''',('Mercades Benz',))# patsapros

# cursor.execute('''SELECT car, motor, company_name FROM cars
# JOIN company USING(copmany_id)
# WHERE copmany_id=(SELECT copmany_id FROM company WHERE company_name=?)''',('Mercades Benz',))# patsapros


result = cursor.fetchall()# barcha ma'lumotni olish
print(result)


db.commit()
db.close()