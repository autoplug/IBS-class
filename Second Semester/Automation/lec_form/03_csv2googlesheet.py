from misc.google import create_service
from googleapiclient.http import MediaFileUpload
import os

# https://developers.google.com/drive/api/guides/manage-uploads

CLIENT_SECRET_FILE_PATH = 'tokens/google_drive_token.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPE = ['https://www.googleapis.com/auth/drive']

def get_csv_files(folder_paths):
    all_files = os.listdir(folder_paths)
    return list(filter(lambda file_name: file_name.endswith('.csv'), all_files))

def export_csv_files(service, file_path, parents):
    file_metadata = {
        'name': os.path.basename(file_path).replace('.csv',''),
        'mimeType': 'application/vnd.google-apps.spreadsheet', # https://developers.google.com/drive/api/guides/mime-types
        'parents': parents
    }

    media = MediaFileUpload(
        filename=file_path,
        mimetype="text/csv"
    )

    service.files().create(
        body=file_metadata,
        media_body=media
    ).execute()

    print(f"csv {os.path.basename(file_path)} was just uploaded as a GoogleSheet...")

if __name__ == '__main__':
    service = create_service(
        CLIENT_SECRET_FILE_PATH,
        API_NAME,
        API_VERSION,
        SCOPE,
        token_folder='tokens'
    )

    for csv_file in get_csv_files('files/'):
        export_csv_files(service=service, file_path=f"files/{csv_file}", parents=['13E9vA4xw_PskC0nJRNQNDCVOvQi3K49y'])