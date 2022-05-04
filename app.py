import flask
from flask import request
from chat import get_response, bot_name

# app = flask.Flask(__name__)

# @app.route('/', methods=['GET'])
# def helloworld():
#     return 'Hello World'

if __name__ == "__main__":
    while(1) :
        msg = input("Enter Msg to Chatbot \n")
        print(get_response(msg))