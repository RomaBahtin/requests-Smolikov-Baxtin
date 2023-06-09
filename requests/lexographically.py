from flask import Flask, request

app = Flask(__name__)


@app.route('/lexographically/', methods=['POST'])
def hello_world():
    a = request.json['a']
    b = request.json['b']
    a = a.lower()
    b = b.lower()
    s = 0

    for i in range(len(a)):
        if ord(a[i]) == ord(b[i]):
            s+=1
        elif ord(a[i]) > ord(b[i]):
            return {'res':1
                    }
        elif ord(a[i]) < ord(b[i]):
            return {'res':-1}

    if s == len(a):
        return {'res':0}

app.run(host='0.0.0.0', port=5000)