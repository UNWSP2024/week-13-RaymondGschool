import sqlite3

connection = sqlite3.connect('phone_book.db')
cursor = connection.cursor()

cursor.execute("create table if not exists Contacts (id integer primary key autoincrement, name text, phone_number text, email text)")

cursor.executemany("insert into Contacts (name, phone_number, email) values (?, ?, ?)", \
[
    ("John Doe", "j123-456-7890", "john.doe@gmail.com"),
    ("Jane Smith", "js123-456-7890", "jane.smith@gmail.com"),
    ("Alice Johnson", "a123-456-7890", "alice.johnson@gmail.com"),
    ("Bob Brown", "b123-456-7890", "bob.brown@gmail.com"),
    ("Charlie Davis", "c123-456-7890", "charlie.davis@gmail.com"),
])

connection.commit()
connection.close()
