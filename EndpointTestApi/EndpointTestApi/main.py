import logging

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/facture/liste', methods=['GET'])
def factureList():
    return 200

@app.route('/facture', methods=['POST'])
def postFacture(factureName):
    return 200


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
