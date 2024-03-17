import sqlite3


def create_dogs_table():
    connection = sqlite3.connect("dogs_database.db", isolation_level=None)
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE dogs (
                        id INTEGER PRIMARY KEY,
                        name TEXT,
                        breed TEXT,
                        age INTEGER,
                        gender TEXT
                    )''')
    return connection


def insert_dog(connection, name, breed, age, gender):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO dogs (name, breed, age, gender) VALUES (?, ?, ?, ?)", (name, breed, age, gender))
