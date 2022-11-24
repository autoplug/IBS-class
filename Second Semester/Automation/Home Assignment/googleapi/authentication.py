import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


class Authentication:
    creds = None

    def __init__(self):
        # If modifying these scopes, delete the file token.json.
        # "https://www.googleapis.com/auth/script.deployments.readonly"
        # "https://www.googleapis.com/auth/script.deployments"
        # "https://www.googleapis.com/auth/script.scriptapp"
        # "https://www.googleapis.com/auth/script.external_request"
        # "https://www.googleapis.com/auth/script.cpanel"
        # "https://www.googleapis.com/auth/drive.scripts "
        # "https://www.googleapis.com/auth/script.projects"
        # "https://www.googleapis.com/auth/script.projects.readonly"
        SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly',
                  'https://www.googleapis.com/auth/spreadsheets',
                  'https://www.googleapis.com/auth/drive',
                  'https://www.googleapis.com/auth/analytics.readonly',
                  "https://www.googleapis.com/auth/forms.body",
                  "https://www.googleapis.com/auth/forms.responses.readonly",
                  "https://www.googleapis.com/auth/script.projects",
                  "https://www.googleapis.com/auth/script.cpanel",
                  "https://www.googleapis.com/auth/script.external_request",
                  "https://www.googleapis.com/auth/drive.scripts",
                  "https://www.googleapis.com/auth/script.scriptapp",
                  "https://www.googleapis.com/auth/script.webapp.deploy",
                  "https://www.googleapis.com/auth/script.deployments"]
        creds = None
        if os.path.exists('json/token.json'):
            creds = Credentials.from_authorized_user_file(
                'json/token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'json/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('json/token.json', 'w') as token:
                token.write(creds.to_json())
        self.creds = creds
