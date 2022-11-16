from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapi.authentication import Authentication


class Sheet(Authentication):
    spreadsheetId = None
    service = None

    def __init__(self):
        super().__init__()
        self.service = build('sheets', 'v4', credentials=self.creds)

    def create(self, title):
        try:
            body = {'properties': {'title': title}}
            spreadsheet = self.service.spreadsheets()
            spreadsheet = spreadsheet.create(body=body, fields='spreadsheetId')
            spreadsheet = spreadsheet.execute()
            self.spreadsheetId = spreadsheet.get('spreadsheetId')
            return self.spreadsheetId
        except HttpError as error:
            print(f"An error occurred: {error}")

    def get(self, ranges=[]):
        response = self.service.spreadsheets()
        response = response.get(
            spreadsheetId=self.spreadsheetId, ranges=ranges, includeGridData=False)
        response = response.execute()
        return response

    def update(self, range, values):
        data = {'values': values}
        response = self.service.spreadsheets().values().update(
            spreadsheetId=self.spreadsheetId,
            body=data,
            range=range,
            valueInputOption='USER_ENTERED').execute()

        return response

    def append(self, range, values):
        data = {'values': values}
        response = self.service.spreadsheets().values().append(
            spreadsheetId=self.spreadsheetId,
            body=data,
            range=range,
            valueInputOption='USER_ENTERED').execute()
