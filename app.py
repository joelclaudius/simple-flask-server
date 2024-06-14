from flask import Flask, request, jsonify

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


@app.route('/questions', methods=['GET', 'POST'])
def questions():
    if request.method=='GET':
        if len(question_list) >0:
            return jsonify(question_list)
        else:
            'Nothing Found', 404

    if request.method=='POST':
        new_question=request.form['question']
        new_option=request.form['options']
        new_correctOption=request.form['correctOption']
        new_point=request.form['points']
        iD= question_list[-1]['id']+1

        new_obj={
            'id':iD,
            'question':new_question,
            'options':new_option,
            'correctOption': new_correctOption,
            'points':new_option
        }

        question_list.append(new_obj)

        return jsonify(question_list), 201




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