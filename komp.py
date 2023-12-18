import sqlite3
import json


db = sqlite3.connect('komp.db')

cursor = db.cursor()

# cursor.execute('''CREATE TABLE IF NOT EXISTS komp(
#     komp_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     title TEXT,
#     link TEXT,
#     image text,
#     price INTEGER
#     )''')
#
# with open('komp.json', mode='r', encoding='utf-8') as file:
#     content = json.load(file)
#
# for news in content:
#     title = news['title']
#     link = news['link']
#     image = news['image']
#     price = news['price']
#     cursor.execute('''INSERT INTO komp(title,link,image,price)
# VALUES(?, ?, ?, ?)''', (title, link, image, price))


db.commit()
db.close()