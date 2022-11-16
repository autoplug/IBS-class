# pip install html5lib
# pip install requests
# pip install bs4

import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")
results = results.find_all("div", class_="is-half")
print(vars(results))
