from flask import Flask, render_template
import requests
import json

page = requests.get("https://api.le-systeme-solaire.net/rest/bodies/")

data = json.loads(page.content)

app = Flask(__name__)


save_result = {}


@app.route("/planets/<name>")
def planets(name):
    name = name.lower()
    result = {"moons": 0}

    for body in data["bodies"]:
        if body["englishName"].lower() == name:
            if body["moons"] != None:
                result["moons"] = len(body["moons"])

            result["mass"] = f"{body['mass']['massValue']} * 10^{body['mass']['massExponent']} kg"
            result["volume"] = f"{body['vol']['volValue']} * 10^{body['vol']['volExponent']} km3"

            if name in save_result:
                save_result[name] += 1
            else:
                save_result[name] = 1

            return result
    return f"I can not find your planet : {name}", 404


@app.route("/usage")
def usage():
    return render_template("index.html", save_result=save_result)


app.run(port=5000, debug=True)
