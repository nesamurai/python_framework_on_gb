import sqlite3


conn = sqlite3.connect('education.db')
cursor = conn.cursor()
cursor.execute("DROP TABLE IF EXISTS student")
sql = '''CREATE TABLE student(
    id INTEGER UNIQUE,
    name TEXT NOT NULL,
    purse INTEGER,
    grade TEXT,
    courses NULL,
    age INTEGER
)'''
cursor.execute(sql)
conn.commit()
conn.close()
