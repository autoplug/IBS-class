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

print(dir(service))
