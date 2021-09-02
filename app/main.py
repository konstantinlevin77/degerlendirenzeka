from flask import Flask
from flask import render_template


from flask_cors import CORS
from .model_api import model_api
from .database_api import database_api


app = Flask(__name__)
CORS(app)
app.register_blueprint(model_api)
app.register_blueprint(database_api)


@app.route("/",methods=["GET"])
def main_page():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
