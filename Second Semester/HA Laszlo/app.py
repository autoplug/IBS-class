from crwal_web import crawl_web
from googleapi import create, update_values

names = crawl_web()

# read this 3 links for googleapi
# https://developers.google.com/sheets/api/quickstart/python
# https://developers.google.com/sheets/api/guides/create
# https://developers.google.com/sheets/api/guides/values

sheetId = create("My spreadsheet")

update_values(sheetId, "A1", [[""]+names])
