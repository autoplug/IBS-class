from misc.google import create_service

CLIENT_SECRET_FILE_PATH = 'tokens/google_drive_token.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPE = ['https://www.googleapis.com/auth/drive']

service = create_service(
    CLIENT_SECRET_FILE_PATH,
    API_NAME,
    API_VERSION,
    SCOPE,
    token_folder='tokens'
)

national_parks = ['Yellow Stone', 'Rocky Mountains', 'Yosemite']

for national_park in national_parks:
    file_metadata = {
        'name': national_park,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': ['13E9vA4xw_PskC0nJRNQNDCVOvQi3K49y']
    }

    service.files().create(body=file_metadata).execute()

    print(f'folder {national_park} was uploaded...')
