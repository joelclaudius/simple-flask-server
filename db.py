import sqlite3

conn = sqlite3.connect('questions.sqlite')
cursor = conn.cursor()

# Correct SQL query to create the table
sql_query = """ 
CREATE TABLE IF NOT EXISTS question (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    options TEXT NOT NULL,
    correctOption INTEGER NOT NULL,
    points INTEGER NOT NULL
)"""

cursor.execute(sql_query)
conn.commit()
conn.close()
