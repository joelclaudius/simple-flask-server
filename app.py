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
    if request.method == 'GET':
        for question in question_list:
            if question['id']==id:
                return jsonify(question)
            pass

    if request.method == 'PUT':
        for question in question_list:
            if question['id']==id:
                question['question']=request.form['question']
                question['options']=request.form['options']
                question['correctOption']=request.form['correctOption']
                question['points']= request.form['points']

                updated_question={
                    'id':id,
                    'question':question['question'],
                    'options':question['options'],
                    'correctOption':question['correctOption'],
                    'points':question['points']
                }
                return jsonify(updated_question)
            
    if request.method =='DELETE':
        for index, question in enumerate(question_list):
            if question['id']==id:
                question_list.pop(index)
                return jsonify(question_list)
            




if __name__ =='__main__':
    app.run(debug=True)