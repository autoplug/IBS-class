from datetime import date, timedelta
import requests
from bs4 import BeautifulSoup

def extracting():
    current_week = date.today()+timedelta(days=-date.today().weekday()+5)

    weeks = [current_week - timedelta(days=i*7) for i in range(4)]
    ranking = []

    for week in weeks:

        page = requests.get("https://www.billboard.com/charts/artist-100/"+str(week))
        soup= BeautifulSoup(page.content, "html.parser")
            
        artist = soup.find_all("div", class_= "o-chart-results-list-row-container")


        for j in range(5):
            first_artist = artist[j].find("h3", id="title-of-a-story").text.strip()
            if  first_artist not in ranking:
                ranking.append(first_artist)

        ranking.sort()

    return(ranking)

#######################################################################






