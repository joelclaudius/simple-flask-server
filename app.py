from flask import Flask, request, jsonify
import sqlite3
import json

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = sqlite3.connect('questions.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

@app.route('/questions', methods=['GET'])
def get_questions():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM question")
    questions = [
        {
            'id': row[0],
            'question': row[1],
            'options': json.loads(row[2]),  # Convert JSON string to list
            'correctOption': row[3],
            'points': row[4]
        }
        for row in cursor.fetchall()
    ]
    conn.close()
    return jsonify({'questions': questions})

if __name__ == '__main__':
    app.run(debug=True)
