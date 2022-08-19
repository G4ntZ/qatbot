from flask import Flask, request, url_for
from connect import connect

app = Flask(__name__)

@app.route('/')
def index():
    return "hola mundo"

@app.route('/bot/<jira>', methods=['GET', 'POST'])
def bot(jira):
    connect()
    if request.method == 'GET':
        return f"GET {jira}"
    else:
        return f"POST {jira}"

