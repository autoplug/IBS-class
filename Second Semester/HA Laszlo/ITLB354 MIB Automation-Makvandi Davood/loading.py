from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"
SAMPLE_RANGE_NAME = "Class Data!A2:E"


def loading(values):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'creds.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    spreadsheet_id = None
    try:
        f = open("spreadsheet_id.txt", "r", encoding='utf-8')
        spreadsheet_id = f.read()
        f.close()
    except IOError:
        pass
    if spreadsheet_id is None:
        try:
            service = build('sheets', 'v4', credentials=creds)
            spreadsheet = {
                'properties': {
                    'title': "Billboard ranking list"
                }
            }
            spreadsheet = service.spreadsheets().create(body=spreadsheet,fields='spreadsheetId').execute()   
            print(f"Spreadsheet ID: {(spreadsheet.get('spreadsheetId'))}")
            spreadsheet_id = spreadsheet.get('spreadsheetId')
        
        except HttpError as error:
            print(f"An error occurred: {error}")
    with open("spreadsheet_id.txt", "w") as f:
        f.write(spreadsheet_id)    
    try:

        service = build('sheets', 'v4', credentials=creds)
        body = {
            'values': values
        }
        range_name = "A1"
        value_input_option = "USER_ENTERED"



        result = service.spreadsheets().values().append(
            spreadsheetId=spreadsheet_id, range=range_name,
            valueInputOption=value_input_option, body=body).execute()
        print(f"{result.get('updatedCells')} cells updated.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error

