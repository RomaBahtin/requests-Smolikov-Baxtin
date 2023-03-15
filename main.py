from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():

    a = 0
    b = request.json['data']
    for i in range(len(b)):
        a += b[i]

    c = {'sum':a}

    return c


app.run()

