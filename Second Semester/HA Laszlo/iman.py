import requests
import json


def weatherStation(keyword):
    LINK = f"https://jsonmock.hackerrank.com/api/weather/search?name={keyword}"
    page = requests.get(LINK)

    response = json.loads(page.content)
    total = response["total"]
    data = response["data"]
    result = []
    for item in data:
        name = item["name"]
        weather = item["weather"].replace("degree", "").strip()
        status = item["status"]
        wind = status[0].replace("Wind:", "").replace("Kmph", "").strip()
        humidity = status[1].replace("Humidity:", "").replace("%", "").strip()
        result.append(f"{name},{weather},{wind},{humidity}")
    return result
