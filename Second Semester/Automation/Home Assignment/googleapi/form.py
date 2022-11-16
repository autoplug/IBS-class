from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapi.authentication import Authentication


class Form(Authentication):
    formId = None

    def __init__(self, title):
        super().__init__()
        form_service = build('forms', 'v1', credentials=self.creds)

        # Request body for creating a form
        NEW_FORM = {
            "info": {
                "title": title,
            }
        }
        # Request body to add a multiple-choice question
        NEW_QUESTION = {
            "requests": [{
                "createItem": {
                    "item": {
                        "title": "In what year did the United States land a mission on the moon?",
                        "questionItem": {
                            "question": {
                                "required": True,
                                "choiceQuestion": {
                                    "type": "RADIO",
                                    "options": [
                                        {"value": "1965"},
                                        {"value": "1967"},
                                        {"value": "1969"},
                                        {"value": "1971"}
                                    ],
                                    "shuffle": True
                                }
                            }
                        },
                    },
                    "location": {
                        "index": 0
                    }
                }
            }]
        }

        result = form_service.forms().create(body=NEW_FORM).execute()
        self.formId = result["formId"]
        question_setting = form_service.forms().batchUpdate(
            formId=result["formId"], body=NEW_QUESTION).execute()
