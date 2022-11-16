from bs4 import BeautifulSoup
from httpx import head
import requests

url = 'https://www.amazon.com/s?k=kindle'

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "DNT": "1",
    "Connection": "close",
    "Upgrade-Insecure-Requests": "1"
    }

page = requests.get(url, headers=HEADERS)


soup = BeautifulSoup(page.content, 'html.parser')

# #class="a-section a-spacing-small a-spacing-top-small"
# print(page.content)
sections = soup.find_all('div', class_ = "sg-col-inner")

print(len(sections))

# print(sections)
# results = []
# for section in sections:
#     title = section.find('span', class_ = 'a-size-medium a-color-base a-text-normal')
#     print(title.text)
#     rate = sections.find('span', class_ = 'a-icon-alt')
#     print(rate.text)
#     price = sections.find('span', class_= 'a-price-whole')
#     print(price.text)
#     fraction = sections.find('span', class_ = 'a-price-fraction')
#     print(fraction.text)
#     results.append({'Title':title.text, 'Rate':rate.text, 'Total price': price.text+'.'+fraction.text})

# print(results)
