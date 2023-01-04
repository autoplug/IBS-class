from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/')
def index():
    args = request.args
    print(args)
    return render_template("/index.html", name="alireza")


@app.route("/planets/<name>", methods=['GET'])
def planets(name):
    page = requests.get("https://api.le-systeme-solaire.net/rest/bodies/")
    return


page = requests.get("https://api.le-systeme-solaire.net/rest/bodies/")
bodies = json.loads(page.content)
for key in bodies:
    print(key)

app.run(port=5000, debug=True, host="localhost")
