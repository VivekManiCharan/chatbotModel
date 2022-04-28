from crypt import methods
import re
import flask
from flask import request
from chat import get_response, bot_name

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello'

# if __name__ == "__main__":
#     msg = input("Enter Msg to Chatbot")
#     print(get_response(msg))