from datetime import date, timedelta
from bs4 import BeautifulSoup
import requests

# chart-date-picker


class Billboard():
    Link = "https://www.billboard.com/charts/artist-100/"
    weeks = []
    artists = []

    def __init__(self):
        week_1st = date.today()
        week_1st += timedelta(days=-date.today().weekday() + 5)
        self.weeks = [week_1st+timedelta(days=-7*i) for i in range(0, 4)]

        # convert date to string
        self.weeks = [d.strftime("%Y-%m-%d") for d in self.weeks]

        for i in range(0, 4):
            Link = self.Link + self.weeks[i]
            page = requests.get(Link)
            soup = BeautifulSoup(page.content, "html.parser")
            rows = soup.find_all(
                "div", class_="o-chart-results-list-row-container")
            if len(rows) > 5:
                for index in range(0, 5):
                    self.artists.append(rows[index].find("h3").text.strip())

        # remove duplicates
        self.artists = list(set(self.artists))

        # sort artists
        self.artists.sort()
