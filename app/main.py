from flask import Flask
from markupsafe import escape
from chat import get_response

app = Flask(__name__)



@app.route("/<msg>")
def response(msg):
    return f"Response {get_response(msg)}"


