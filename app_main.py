from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
from forms import formDict

app = FastAPI()

pageNumber = 0


def send_email():
    # send email
    return


@app.post("/begin_session")
def begin_session():
    global pageNumber
    pageNumber = 0
    return {
        "bookingId": "1234567890",
        "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
        "questionnaire": {
            "name": "initial_information",
            "items": [
                {
                    "id": "admissionDate",
                    "t": "Date",
                    "type": "string",
                    "req": True,
                    "value": ""         
                },
                {
                    "id": "admittedBy",
                    "t": "Admitted by",
                    "type": "string",
                    "req": True,
                    "value": ""       
                },
                {
                    "id": "admissionType",
                    "t": "Admission Type",
                    "type": "checkbox",
                    "options": ["Re-Admit", "New Admit"],
                    "req": True
                },
                {
                    "id": "admissionMethod",
                    "t": "Admission was",
                    "type": "checkbox",
                    "options": ["In Person", "Virtual", "Phone"],
                    "req": True
                }
            ]
        }
    }

@app.post("/information_advance")
def information_advance(data: dict[Any, Any]):
    global pageNumber
    # write information to database
    if len(formDict) == pageNumber:
        send_email()
        return {"message": "All information has been submitted. Agreement form has been sent to email"}
    pageNumber += 1
    return formDict[pageNumber]

@app.post("/end_session")
def end_session():
    global pageNumber
    pageNumber = len(formDict)
    send_email()
    return {"message": "The current information provided has been submitted. Agreement form has been sent to email"}