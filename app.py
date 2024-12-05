from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proxy', methods=['POST'])
def proxy():
    URL = "https://superiorapis-creator.cteam.com.tw/manager/feature/proxy/7bb3a1c75f960f131f3ea67515e83a7ba2/pub_20d708b5c860ee18a675160fd8f2c9"
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJjZXJ0IjoiYWU0YTA3M2M0YTdmZWE0Y2Y1OTFmZGE5YTQ0MTFmZjNhM2U3NDgxOSIsImlhdCI6MTczMzM4NTg1OX0.QyOSkHgbXfFUnl6J7vpgoPe96t-JmWGqiKTCkH7aryg"
    
    headers = {
        'Content-Type': 'application/json',
        'token': token
    }
    
    response = requests.post(URL, json=request.json, headers=headers)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
