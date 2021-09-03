from flask import Blueprint,request,jsonify

from .QuestionsDao import QuestionsDao
from .Question import Question

from .AnswersDao import AnswersDao
from .Answer import Answer

import os

database_api = Blueprint("database_api",__name__)

API_KEY = os.environ["API_KEY"]

# WITH API KEY
@database_api.route("/api/database/addQuestion",methods=["POST"])
def add_question():
    content = request.json
    if content is not None:
        if content.get("api_key") == API_KEY:
            if content.get("question") is not None:
                new_question = Question(question_text=content.get("question"))
                dao = QuestionsDao()
                dao.add(new_question)
                return jsonify({"result":"Successful"})
    return jsonify({"result":"Failed"})

@database_api.route("/api/database/deleteQuestionById",methods=["POST"])
def delete_question_by_id():
    id_value = request.args.get("id")
    api_key = request.args.get("apikey")
    if id_value is not None:
        if api_key == API_KEY:
            dao = QuestionsDao()
            dao.delete(Question(id=id_value))
            return jsonify({"result":"Successful"})
    return jsonify({"result":"Failed"})


# WITHOUT API KEY
@database_api.route("/api/database/addAnswer",methods=["POST"])
def add_answer():
    content = request.json
    if content is not None:
        if content.get("answer") is not None:
            if content.get("question_id") is not None:
                new_answer = Answer(question_id=content.get("question_id"),
                answer=content.get("answer")
                )
                dao = AnswersDao()
                dao.add(new_answer)
                return jsonify({"result":"Successful"})
    return jsonify({"result":"Failed"})


# WITH API KEY
@database_api.route("/api/database/getAllAnswers",methods=["GET"])
def get_all_answers():
    key = request.args.get("apikey")
    if key == API_KEY:
        results = []
        dao = AnswersDao()
        for r in dao.find_all():
            results.append({
                "id":r.id,
                "question_id":r.question_id,
                "answer":r.answer
                })

        return jsonify(results)
    return None

# WITH API KEY
@database_api.route("/api/database/getAllQuestions",methods=["GET"])
def get_all_questions():
    key = request.args.get("apikey")

    if key == API_KEY:
        results = []
        dao = QuestionsDao()
        for r in dao.find_all():

            value_in_json_format = {
                "id":r.id,
                "question_text":r.question_text
            }

            print(value_in_json_format)
            results.append(value_in_json_format)
        return jsonify(results)

    print("WRONG API KEY!")
    return []
