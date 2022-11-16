# https://developers.google.com/drive/api/v3/reference/files/create
# https://stackoverflow.com/questions/13558653/how-can-i-create-a-new-folder-with-google-drive-api-in-python

from Google import Create_Service

CLIENT_SECRET_FILE = "secrets.json"
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(
    CLIENT_SECRET_FILE,
    API_NAME,
    API_VERSION,
    SCOPES
    )

national_parks = ["Yellow Stone", "rocky Mountains", "Yosemite"]

for national_park in national_parks:

    file_matadata = {
        'name': national_park,
        'mimeType': 'application/vnd.google-apps.folder', # https://developers.google.com/drive/api/guides/mime-types
        'parents': ['13E9vA4xw_PskC0nJRNQNDCVOvQi3K49y']
    }

    service.files().create(body=file_matadata).execute()

    print(f"Folder {national_park} was created successfully...")