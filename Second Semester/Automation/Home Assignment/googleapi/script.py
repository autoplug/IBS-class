from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapi.authentication import Authentication
import requests


class Script(Authentication):
    scriptId = None
    SAMPLE_CODE = '''
    function myFunction() {
      var sheet = SpreadsheetApp.openById(
    getId('TopRanks')
    );
    sheet.appendRow(["hhhhhhhhh", "css004"]);
    }
    function getId(name) {
        var myFiles = DriveApp.searchFiles('"me" in owners');
        var result = "";
        while (myFiles.hasNext()) {
            var file = myFiles.next();
            if (file.getName() == name) result = file.getId();
        }
        return result;
    }
    '''.strip()

    SAMPLE_MANIFEST = '''
    {
    "timeZone": "America/New_York",
    "exceptionLogging": "CLOUD"
    }
    '''.strip()

    def __init__(self):
        super().__init__()
        # with open("gs/create.gs.js") as sc:
        #     self.SAMPLE_CODE = sc.read()

        self.service = build('script', 'v1', credentials=self.creds)

    def create(self, title):
        try:
            request = {'title': title}
            response = self.service.projects().create(body=request).execute()
            self.scriptId = response['scriptId']
            # Upload two files to the project
            request = {
                'files': [{
                    'name': title,
                    'type': 'SERVER_JS',
                    'source': self.SAMPLE_CODE
                }, {
                    'name': 'appsscript',
                    'type': 'JSON',
                    'source': self.SAMPLE_MANIFEST
                }]
            }
            response = self.service.projects().updateContent(
                body=request,
                scriptId=response['scriptId']).execute()
            self.scriptId = response['scriptId']
            return response['scriptId']
        except HttpError as error:
            print(error.content)

    def run(self):
        request = {"function": "myFunction"}
        params = {}
        request = {'function': 'some_function', 'parameters': params}
        try:
            response = self.service.scripts().run(
                body=request, scriptId=self.scriptId).execute()
            if response.get('error'):
                message = response['error']['details'][0]['errorMessage']
                print(message)
        except HttpError as error:
            print(error)

        # res = requests.post(
        #     f"https://script.googleapis.com/v1/scripts/{self.scriptId}:run")
