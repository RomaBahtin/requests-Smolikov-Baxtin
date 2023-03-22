from flask import Flask, request

app = Flask(__name__)


@app.route('/sum3/', methods=['POST'])
def hello_world():
    b = request.json.values()
    d = sum(b)

    c ={'sum': d}

    return c




app.run(host='0.0.0.0', port=5000)