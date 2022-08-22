from flask import Flask, request, url_for
from connect import Connect
from Pauta import Pauta

app = Flask(__name__)

@app.route('/bot/<jira>', methods=['GET', 'POST'])
def bot(jira):
    con = Connect()
    if request.method == 'GET':
        return f"GET {jira}"
    else:
        return f"POST {jira}"

@app.route('/pauta/<pautaJira>', methods=['GET'])
def pauta(pautaJira):
    pauta = Pauta(pautaJira)
    return pauta.html_tab
