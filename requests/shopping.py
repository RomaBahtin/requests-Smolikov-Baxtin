from flask import Flask, request

app = Flask(__name__)

mega_list = dict()

@app.route('/shoppinglist/new/', methods=['POST'])
def hello_world():
    k=request.json['new_list']
   # mega_list[k] = {}
    if k not in mega_list:
        mega_list.append(k)
    else:
        return {'status' : 'fail'}
    return {'status' : 'ok'}







#    mega_list = request.json
 #   print(mega_list['new_list'])
#    id_list.append(mega_list['new_list'])
#    print(id_list)
#    for i in range(len(id_list)):
#        if mega_list['new_list'] in id_list:
 #           c = {'status': 'fail'}
 #           return c
 #       else:
 #           c = {'status': 'ok'}
 #           return c


shopping_list = dict()
@app.route('/shoppinglist/add/', methods=['POST'])
def hello_world2():
    shopping_list.update({request.json['data']})
    print(shopping_list)
    #shopping_list = {mega_list['new_list']:{request.json['data']}}
    print(shopping_list)
    return shopping_list

# @app.route('/shoppinglist/getlist/', methods=['POST'])
# def hello_world3():
# requests.post(host + url_getlist, json={'list': 1})





app.run(host='0.0.0.0', port=5000)


