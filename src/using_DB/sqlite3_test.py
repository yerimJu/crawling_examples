import sqlite3 # standard library for Python

DB_PATH = 'test.sqlite'
conn = sqlite3.connect(DB_PATH)

cur = conn.cursor()
cur.executescript('''
DROP TABLE IF EXISTS items;

CREATE TABLE items(
    item_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE,
    price INTEGER
);

INSERT INTO items(name, price) VALUES ('Apple', 800);
INSERT INTO items(name, price) VALUES ('Orange', 700);
INSERT INTO items(name, price) VALUES ('Banana', 600);
''')

# apply db
conn.commit()

cur = conn.cursor()
cur.execute("SELECT item_id, name, price FROM items")
item_list = cur.fetchall()

for it in item_list:
    print(it)
