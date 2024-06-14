import sqlite3
import json

# Function to create database and insert data from JSON
def create_database():
    conn = sqlite3.connect('questions.sqlite')
    cursor = conn.cursor()

    # SQL query to create the table
    sql_query = """ 
    CREATE TABLE IF NOT EXISTS question (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        options TEXT NOT NULL,
        correctOption INTEGER NOT NULL,
        points INTEGER NOT NULL
    )"""

    cursor.execute(sql_query)

    # Load questions from JSON data
    with open('questions.json') as f:
        questions_data = json.load(f)

    # Insert each question into the database
    for question in questions_data['questions']:
        question_text = question['question']
        options = json.dumps(question['options'])  # Convert list to JSON string
        correct_option = question['correctOption']
        points = question['points']

        sql_insert = """INSERT INTO question (question, options, correctOption, points)
                        VALUES (?, ?, ?, ?)"""
        cursor.execute(sql_insert, (question_text, options, correct_option, points))

    conn.commit()
    conn.close()

# Execute the function to create database and insert data
if __name__ == '__main__':
    create_database()
