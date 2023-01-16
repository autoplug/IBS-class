from flask import Flask, render_template
import requests
import json


def get_average(city):
    api_key = "701665084291555433011x24374"
    # without auth key
    # page = requests.get(f"https://geocode.xyz/?locate={city}&json=1")
    page = requests.get(f"https://geocode.xyz/{city}?json=1&auth={api_key}")
    data = json.loads(page.content)
    countryname = data["standard"]["countryname"]
    longtitude = data["longt"]
    latitude = data["latt"]
    print(latitude, longtitude, countryname)

    wheather_api = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longtitude}&hourly=temperature_2m")

    data_temprature = json.loads(wheather_api.content)
    data_temprature = data_temprature["hourly"]["temperature_2m"]
    average_temprature = sum(data_temprature)/len(data_temprature)

    print(average_temprature)
    return average_temprature, countryname


app = Flask(__name__)

global_save_variable = []


@app.route("/temperature/<cityname>")
def temperature(cityname):
    result = {
        "city": cityname,
        "country": "",
        "averagetemp": 0
    }
    averagetemp, country = get_average(cityname)
    result["country"] = country
    result["averagetemp"] = averagetemp

    global_save_variable.append(result)
    return "{" + f'"city":"{cityname}", "country": "{country}", "averagetemp":{averagetemp}' + "}"
    return result


@app.route("/usage")
def usage():
    return render_template("index.html", names=global_save_variable)


app.run(debug=True, port=5000)
