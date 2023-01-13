from flask import Flask, render_template
import requests
import json


def get_by_name(city="budapest"):
    auth_key = "701665084291555433011x24374"
    page = requests.get(
        f"https://geocode.xyz/{city}?geoit=json&json=1&auth={auth_key}")

    data = json.loads(page.content)

    longitude = data["longt"]
    latitude = data["latt"]
    countryname = data["standard"]["countryname"]
    api2 = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m")

    temperature_2m = json.loads(api2.content)["hourly"]["temperature_2m"]
    average = sum(temperature_2m)/len(temperature_2m)
    return average, countryname


app = Flask(__name__)

global_repeat = {}


@app.route("/temperature/<cityname>")
def temperature(cityname):
    average_temperature, countryname = get_by_name(cityname)

    global_repeat[cityname] = {"city": cityname,
                               "country": countryname,
                               "averagetemp": average_temperature}

    return global_repeat[cityname]


@app.route("/usage")
def usage():
    return render_template("index.html", cities=global_repeat)


app.run(port=5000, debug=True)
