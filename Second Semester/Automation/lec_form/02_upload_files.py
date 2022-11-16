from misc.google import create_service
from googleapiclient.http import MediaFileUpload

# https://developers.google.com/drive/api/guides/manage-uploads

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

file_names = ['file01.csv', 'file02.json', 'file03.jpeg']
folder_ids = [
    '1gZELbAhzjGB0ZdN7Cw5bV-yWrajrNbL_',
    '1el4CyS6xZgO6shDUf9IJRsdWfgGSX2CY', 
    '1DgHscuETyFYmSFeAMdyTUrBKvIhblItQ'
    ]
mimetypes = ['text/csv', 'application/json', 'image/jpeg']


for file_name, folder_id, mimetype in zip(file_names, folder_ids, mimetypes):
    file_metadata = {
        'name': file_name,
        'parents': [folder_id]
    }

    media = MediaFileUpload(
        f'files/{file_name}',
        mimetype=mimetype  # https://learndataanalysis.org/commonly-used-mime-types/
    )

    service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
        ).execute()

    print(f'file {file_name} was uploaded...')
