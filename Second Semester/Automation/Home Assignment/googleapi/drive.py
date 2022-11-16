from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapi.authentication import Authentication


class Drive(Authentication):
    service = None

    def __init__(self):
        super().__init__()
        self.service = build('drive', 'v3', credentials=self.creds)

    def files(self):
        try:
            # Call the Drive v3 API
            results = self.service.files().list().execute()
            items = results.get('files', [])

            if not items:
                print('No files found.')
                return None
            return items
        except HttpError as error:
            print(f'An error occurred: {error}')
