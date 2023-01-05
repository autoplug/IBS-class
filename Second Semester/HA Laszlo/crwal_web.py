from bs4 import BeautifulSoup
from datetime import timedelta, datetime
import requests

Link = "https://www.billboard.com/charts/artist-100/"


def crawl_web():
    result = []
    page = requests.get(Link)
    soup = BeautifulSoup(page.content, "html.parser")
    current_week = soup.find("div", id="chart-date-picker")
    current_week = current_week.get("data-date")
    weeks = [datetime.strptime(current_week, '%Y-%m-%d') -
             timedelta(weeks=i+1)for i in range(4)]
    weeks = [str(w)[0:10] for w in weeks]
    for week in weeks:
        page = requests.get(Link + week)
        soup = BeautifulSoup(page.content, "html.parser")
        persons = soup.find_all(
            "div", class_="o-chart-results-list-row-container")
        for person in persons[0:5]:
            name = person.find(id="title-of-a-story")
            result.append(name.text.strip())
    result = list(set(result))
    result.sort()
    return result
