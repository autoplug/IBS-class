import json
from flask import Flask, request, Response  # FastAPI


app = Flask(__name__)


@app.route('/health')
def health():
    # return Response(json.dumps({"message": "I am live"}), mimetype='application/json')
    return {"message": "I am live"}

# kwargs


@app.route('/hello')
def greeting():
    # dict.get() // head, formdata, body, ...
    name = request.args.get('name', 'World')
    return Response(json.dumps({"message": say_hello(name)}), mimetype='application/json')


@app.route('/multiple_method', methods=['GET', 'POST'])
def multiple_method():
    if request.method == 'POST':
        return Response(json.dumps({"message": "It is a POST call"}), mimetype='application/json')
    if request.method == 'GET':
        return Response(json.dumps({"message": "It is a GET call"}), mimetype='application/json')


if __name__ == '__main__':
    app.run(
        host='localhost',
        debug=True,
        port=5000,  # 80 default for browserl
    )

# curl -X GET http://localhost:5000/multiple_method
# curl -X POST http://localhost:5000/multiple_method

# curl http://localhost:5000/hello?name=Me
