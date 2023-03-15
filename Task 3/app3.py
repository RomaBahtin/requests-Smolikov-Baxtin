import requests

host = 'http://127.0.0.1:5000'
r = requests.post(host,
                  json={'a': 1, 'b': 2, 'c': 3})
print( r.json())
assert r.json() == {'sum': 6}

r = requests.post(host,
                  json={'a': 1, 'b': 2})

assert r.json() == {'sum': 3}

r = requests.post(host,
                  json={'d': 1})

assert r.json() == {'sum': 1}

print(r.text)
