from googleapi.script import Script
from googleapi.sheet import Sheet
from googleapi.drive import Drive
from crawl.billboard import Billboard

#
#
#
# Get the List of celebrities
topRanks = Billboard()

#
#
#
# Check If There is
drive = Drive()
files = drive.files()
sheetID = None
scriptId = None
for file in files:
    if file["name"] == "TopRanks":
        sheetID = file["id"]
    if file["name"] == "script":
        scriptId = file["id"]

#
#
#
# create spreadsheet
excel_sheet = Sheet()
if sheetID is None:
    excel_sheet.create("TopRanks")
else:
    excel_sheet.spreadsheetId = sheetID
    print("sheetID", sheetID)

excel_sheet.append("A1", [["", ""]+[f"{topRanks.weeks[0]}"]+topRanks.artists])


script = Script()
if scriptId is None:
    script.create("script")
    print("You need To run the script file inside of google drive to get the permissions to it.")
else:
    script.scriptId = scriptId
    print("scriptId", scriptId)

script.run()
print("End")
