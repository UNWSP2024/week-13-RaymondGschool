import sqlite3

connection = sqlite3.connect('cities.db')
cursor = connection.cursor()

cursor.execute("create table if not exists Cities (id integer primary key autoincrement, name text, country text, population integer)")

cursor.executemany("insert into Cities (name, country, population) values (?, ?, ?)", \
[
    ('New York', 'USA', 100),
    ('London', 'UK', 200),
    ('Tokyo', 'Japan', 300),
    ('Sydney', 'Australia', 400),
    ('Mumbai', 'India', 500)
])

connection.commit()
connection.close()
