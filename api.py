import flask
from flask import request, jsonify
from FileUtils import read_users
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return jsonify(read_users(3))


app.run()
