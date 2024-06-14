from flask import Flask, request, jsonify
import json
import sqlite3

app = Flask(__name__)

question_list=[
    {
        "id":0,
      "question": "Which is the most popular JavaScript framework?",
      "options": "Angular",
      "correctOption": 1,
      "points": 10
    },
    {
        "id":1,
      "question": "Which company invented React?",
      "options": "Google",
      "correctOption": 3,
      "points": 10
    },
    {
            "id":2,
      "question": "What's the fundamental building block of React apps?",
      "options": "Components",
      "correctOption": 0,
      "points": 10
    },
    {
             "id":3,
     "question": "What's the name of the syntax we use to describe the UI in React components?",
      "options": "FBJ", 
      "correctOption": 2,
      "points": 10
    },
    {
              "id":4,
    "question": "How does data flow naturally in React apps?",
      "options": 
        "From parents to children",
    
      "correctOption": 5,
      "points": 10
    },
    {
                "id":6,
      "question": "How to pass data into a child component?",
      "options": "State", 
      "correctOption": 1,
      "points": 10
    },]

def db_connection():
    conn = None
    try:
        conn=sqlite3.connect('questions.sqlite')
    except sqlite3.error as e:
        print(e)
    return conn

@app.route('/questions', methods=['GET', 'POST'])
def questions():
    conn = db_connection()
    cursor = conn.cursor()
    if request.method=='GET':
        cursor=conn.execute("SELECT * FROM question")
        questions = [
            dict(id=row[0], question=row[1], options=row[2], correctOption=row[3], point=row[4])
            for row in cursor.fetchall()
        ]
        if questions is not None:
            return jsonify(questions)


    if request.method=='POST':
        new_question=request.form['question']
        new_option=request.form['options']
        new_correctOption=request.form['correctOption']
        new_point=request.form['points']
        
        sql = """INSERT INTO question (question, options, correctOption, points)
                VALUES(?, ?, ?, ?)"""

        cursor= conn.execute(sql, (new_question, new_option, new_correctOption, new_point))
        conn.commit()
        return f"Book with id: {cursor.lastrowid} created successifully", 201



@app.route('/question/<int:id>', methods=['GET','PUT','DELETE'])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    question=None

    if request.method == 'GET':
        cursor.execute("SELECT * FROM question WHERE id=?", (id,))
        rows = cursor.fetchall()
        for r in rows:
            question=r
        if question is not None:
                return jsonify(question), 200
        else:
            return'Something went wrong', 404

    if request.method == 'PUT':
        sql = """ UPDATE question
                SET question=?,
                    options=?,
                    correctOption=?,
                    points=?
                WHERE id=?"""
        
        question=request.form['question']
        options=request.form['options']
        correctOption=request.form['correctOption']
        points= request.form['points']

        updated_question={
            'id':id,
            'question':question,
            'options':options,
            'correctOption':correctOption,
            'points':points
        }
        conn.execute(sql, (question, options, correctOption, points, id))
        conn.commit()
        return jsonify(updated_question)
            
    if request.method =='DELETE':
        sql=""" DELETE FROM question WHERE id= ? """
        conn.execute(sql, (id,))
        conn.commit()
        return "The book with id: {} has been deleted.".format(id), 200
            




if __name__ =='__main__':
    app.run(debug=True)