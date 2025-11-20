import smtplib
from email.message import EmailMessage
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any
from forms import formDict, userDict

app = FastAPI()

pageNumber = 2

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = "benjaminwang42@gmail.com"       
EMAIL_PASSWORD = "vvmppsbyysncebnv"
RECIPIENT_EMAIL = ""

def deliver_email():
    msg = EmailMessage()
    msg['Subject'] = "Agreement Form"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = RECIPIENT_EMAIL
    msg.set_content("Please fill out the pharmacy agreement at your earliest convenience. Thank you!")

    with open(f"PharmacyAgreement.pdf", "rb") as f:
        file_data = f.read()
        file_name = f.name
    msg.add_attachment(file_data, maintype="application", subtype="pdf", filename=file_name)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")
    return

@app.post("/set_email")
def set_email(data: dict[Any, Any]):
    global RECIPIENT_EMAIL
    args = data["args"]
    email = args.get("emailAddress")
    RECIPIENT_EMAIL = email
    
    print("NEW EMAIL:", RECIPIENT_EMAIL)
    return {"Message": "Email has been recorded"}

@app.post("/send_email")
def send_email():
    deliver_email()
    
    return {"Message": "Email has been sent"}

@app.post("/get_details")
def get_details(data: dict[Any, Any]):
    args = data["args"]
    patient_id = args.get("patient_id")
    if not patient_id:
        raise HTTPException(status_code=400, detail="Missing patient_id")

    patient_details = userDict.get(patient_id)
    
    if not patient_details:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    return patient_details

@app.post("/begin_session")
def begin_session():
    global pageNumber, RECIPIENT_EMAIL
    RECIPIENT_EMAIL = ""
    pageNumber = 0
    return {
        "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
        "questionnaire": {
            "name": "Select Appointment Type",
            "items": [
            {
                "id": "appointmentType",
                "t": "What type of appointment would you like?",
                "type": "select",
                "options": ["In-Store", "Phone", "Virtual"],
                "req": True
            }
            ]
        }
    }

@app.post("/information_advance")
def information_advance(data: dict[Any, Any]):
    global pageNumber, RECIPIENT_EMAIL
    # write information to database
    if len(formDict) == pageNumber:
        return { "message": f"All information has been submitted."}
    
    if data['args'].get('patientUpdates').get('emailAddress'):
        RECIPIENT_EMAIL = data['args'].get('patientUpdates').get('emailAddress')
        print("UPDATING RECIPIENT EMAIL:", RECIPIENT_EMAIL)

    pageNumber += 1
    return formDict[pageNumber]

@app.post("/end_session")
def end_session():
    global pageNumber
    pageNumber = len(formDict)

    deliver_email()
    return { "message": f"All information has been submitted. Agreement form has been sent to {RECIPIENT_EMAIL}"}

