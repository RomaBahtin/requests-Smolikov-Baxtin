from flask import Flask, request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():

    b = request.json.values()
    d = sum(b)
    print(d)

    c = {'sum': d}

    return c


app.run()