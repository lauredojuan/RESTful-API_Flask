

from flask import Flask, jsonify, request
import json

app = Flask(__name__)


todos =[{ "label": "My first task", "done": False },
        { "label": "My second task", "done": False },
        { "label": "My last task", "done": False }] 

@app.route('/todos', methods=['GET'])
def hello_world():

    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)

# @app.route('/todos', methods=['POST'])
# def add_new_todo():
#     request.get_json()
#     return jsonify(request.get_json())


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
 if len(todos) > position:
    todos.pop(position)
    return jsonify(todos)
 else:
    return jsonify(todos)    
        


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
