from flask import Flask
import requests
import json

page = requests.get("https://api.le-systeme-solaire.net/rest/bodies/")

data = json.loads(page.content)

app = Flask(__name__)


repeat = {}


@app.route("/planets/<name>")
def planets(name):
    result = {"moons": 0}

    for body in data["bodies"]:
        if body["englishName"].lower() == name.lower():
            if body["moons"] != None:
                result["moons"] = len(body["moons"])

            result["mass"] = f"{body['mass']['massValue']} * 10^{body['mass']['massExponent']} kg"
            result["volume"] = f"{body['vol']['volValue']} * 10^{body['vol']['volExponent']} km3"

            if name in repeat:
                repeat[name] += 1
            else:
                repeat[name] = 1

            return result
    return f"I can not find your planet : {name}", 404


@app.route("/usage")
def usage():
    result = ""
    for key in repeat:
        result += f" {key} : looked up {repeat[key] } times <br>"

    return result


app.run(port=5000, debug=True)
