from flask import Flask
import requests
import json

page = requests.get("https://api.le-systeme-solaire.net/rest/bodies/")

data = json.loads(page.content)

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello"


# call_planet = []  # Moon, Neptune, Moon
call_planet = {}  # Moon, Neptune, Moon


@app.route("/planets/<name>")
def planets(name):
    result = {
        "moons": 0,
        "mass": ""
    }
    for body in data["bodies"]:
        if body["englishName"].lower() == name.lower():
            if body["moons"] != None:
                result["moons"] = len(body["moons"])

            result["mass"] = f"{body['mass']['massValue']} * 10^{body['mass']['massExponent']} kg"

            # call_planet.append(name)
            if name in call_planet:
                call_planet[name] += 1
            else:
                call_planet[name] = 1

            return result
    return f"I can not find your planet {name}", 404


@app.route("/usage")
def usage():
    # cp = list(set(call_planet))
    # result = ""

    # for item in cp:
    #     result += f"{item}: looked up {call_planet.count(item)} times"
    result = ""
    for key in call_planet:
        result += f"{key}: {call_planet[key] } times <br>"

    return result


app.run(port=5000, debug=True)
