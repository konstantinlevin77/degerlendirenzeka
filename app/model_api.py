from flask import Blueprint,request,jsonify
from .LoadedModel import LoadedModel
from flask_cors import CORS

model_api = Blueprint("model_api",__name__)
CORS(model_api)

model = LoadedModel("./model/finetuned","./model/tokenizer.pickle",53)

@model_api.route("/api/model/predict",methods=["POST"])
def predict():


    content = request.get_json()
    print("POST REQUEST HAS BEEN DONE CONTENT:")
    print(content)
    if content is not None:
        if content.get("answer") is not None:  
            json_return = jsonify(model.predict_answer(content.get("answer")))
            json_return.headers.add("Access-Control-Allow-Origin",'*')


            return json_return

    json = jsonify({
        "answer":None,
        "result":None
    })
    json.headers.add('Access-Control-Allow-Origin', '*')
    return json
   

