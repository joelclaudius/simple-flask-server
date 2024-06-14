import sqlite3

conn = sqlite3.connect('questions.sqlite')

cursor = conn.cursor()
sql_query= """ CREATE TABLE question (
    id interger PRIMARY KEY NOT NULL,
    question text NOT NULL,
    options text NOT NULL,
    correctOption integer NOT NULL,
    points integer NOT NULL
)"""

cursor.execute(sql_query)