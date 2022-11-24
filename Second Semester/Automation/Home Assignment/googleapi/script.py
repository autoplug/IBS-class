from googleapiclient.discovery import build
from googleapi.authentication import Authentication
from googleapiclient import errors


class Script(Authentication):
    scriptId = None
    SAMPLE_CODE = '''
        function myFunction() {
        console.log("Hello, world!");
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
        with open("gs/create.gs.js") as sc:
            self.SAMPLE_CODE = sc.read().strip()

    def create(self, title):
        try:
            self.service = build('script', 'v1', credentials=self.creds)
            # Call the Apps Script API
            # Create a new project
            request = {'title': 'script'}
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
                scriptId=self.scriptId).execute()

            self.scriptId = response['scriptId']
            return self.scriptId
        except errors.HttpError as error:
            # The API encountered a problem.
            print(error.content)

    def run(self):
        # request = {"function": "myFunction"}
        # params = {}
        # request = {'function': 'some_function', 'parameters': params}
        # try:
        #     response = self.service.scripts().run(
        #         body=request, scriptId=self.scriptId).execute()
        #     if response.get('error'):
        #         message = response['error']['details'][0]['errorMessage']
        #         print(message)
        # except HttpError as error:
        #     print(error)
        pass

        # res = requests.post(
        #     f"https://script.googleapis.com/v1/scripts/{self.scriptId}:run")
