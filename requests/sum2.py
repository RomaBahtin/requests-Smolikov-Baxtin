from flask import Flask, request

app = Flask(__name__)


@app.route('/sum2/', methods=['POST'])
def hello_world():
    b = request.json['data']
    d = sum(b)

    c = {'sum': d}
    print(c)
    return c

app.run(host='0.0.0.0', port=5000)