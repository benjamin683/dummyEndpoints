from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any

app = FastAPI()

pageNumber = 0
formDict = { 1 : {}, 2 : {}}
formDict[1] = {
    "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
    "questionnaire": {
        "name": "patient_information_form",
        "items": [
  "Patient Information",
  {
    "id": "patientName",
    "t": "Patient Name",
    "type": "string",
    "req": true,
    "value": ""
  },
  {
    "id": "gender",
    "t": "Gender",
    "type": "checkbox",
    "options": ["Male", "Female"],
    "req": true
  },
  {
    "id": "dob",
    "t": "Date of Birth",
    "type": "string",
    "req": true,
    "value": ""
  },
  {
    "id": "ssn",
    "t": "SSN",
    "type": "string",
    "req": true,
    "value": ""
  },
  {
    "id": "phone",
    "t": "Phone",
    "type": "string",
    "req": true,
    "value": ""
  },
  {
    "id": "email",
    "t": "Email",
    "type": "string",
    "req": true,
    "value": ""
  },

  "Allergies",
  {
    "id": "drugAllergies",
    "t": "Drug Allergies",
    "type": "checkbox",
    "options": ["No Known Drug Allergies", "Drug Allergies"],
    "req": false
  },

  "Packaging Preferences",
  {
    "id": "packagingType",
    "t": "Packaging Type",
    "type": "checkbox",
    "options": ["VIMP", "Bottles", "Spanish"],
    "req": false
  },
  {
    "id": "ezCaps",
    "t": "Patient requests EZ caps",
    "type": "checkbox",
    "options": ["Yes", "No"],
    "req": false
  },

  "Shipping Address",
  {
    "id": "shippingStreet",
    "t": "Street",
    "type": "string",
    "req": true,
    "value": ""
  },
  {
    "id": "shippingCounty",
    "t": "County",
    "type": "string",
    "req": false,
    "value": ""
  },
  {
    "id": "shippingCity",
    "t": "City",
    "type": "string",
    "req": true,
    "value": ""
  },
  {
    "id": "shippingState",
    "t": "State",
    "type": "string",
    "req": true,
    "value": ""
  },
  {
    "id": "shippingZip",
    "t": "ZIP Code",
    "type": "string",
    "req": true,
    "value": ""
  },

  "Billing Address",
  {
    "id": "billingStreet",
    "t": "Street",
    "type": "string",
    "req": true,
    "value": ""
  },
  {
    "id": "billingCounty",
    "t": "County",
    "type": "string",
    "req": false,
    "value": ""
  },
  {
    "id": "billingCity",
    "t": "City",
    "type": "string",
    "req": true,
    "value": ""
  },
  {
    "id": "billingState",
    "t": "State",
    "type": "string",
    "req": true,
    "value": ""
  },
  {
    "id": "billingZip",
    "t": "ZIP Code",
    "type": "string",
    "req": true,
    "value": ""
  },

  "Medication Management",
  {
    "id": "manageOwnMedications",
    "t": "Do you manage your own medications?",
    "type": "checkbox",
    "options": ["Yes", "No"],
    "req": true
  },
  {
    "id": "medManagerName",
    "t": "Medication Manager Name",
    "type": "string",
    "req": true,
    "value": "",
    "when": [
      {
        "operator": "=",
        "question": "manageOwnMedications",
        "answerString": "No"
      }
    ]
  },
  {
    "id": "medManagerRelationship",
    "t": "Relationship to Patient",
    "type": "string",
    "req": true,
    "value": "",
    "when": [
      {
        "operator": "=",
        "question": "manageOwnMedications",
        "answerString": "No"
      }
    ]
  },
  {
    "id": "medManagerPhone",
    "t": "Medication Manager Phone",
    "type": "string",
    "req": true,
    "value": "",
    "when": [
      {
        "operator": "=",
        "question": "manageOwnMedications",
        "answerString": "No"
      }
    ]
  },
  {
    "id": "medManagerEmail",
    "t": "Medication Manager Email",
    "type": "string",
    "req": false,
    "value": "",
    "when": [
      {
        "operator": "=",
        "question": "manageOwnMedications",
        "answerString": "No"
      }
    ]
  }
]

    }
}

formDict[2] = {
    "userId": "7c68d02b-96e3-4083-b559-300c1e910364",
    "questionnaire": {
        "name": "monthly_contact_information_form",
        "items": [
  "Monthly Contact Information",
  {
    "id": "monthlyContactType",
    "t": "Monthly Contact is",
    "type": "checkbox",
    "options": ["Patient", "Family Member", "Other Caregiver"],
    "req": true
  },
  {
    "id": "contactAware",
    "t": "Contact is aware we must speak with them monthly and understands service may be interrupted if we are unable to contact them",
    "type": "checkbox",
    "options": ["Yes", "No"],
    "req": true
  },
  {
    "id": "contactName",
    "t": "Contact Name (if other than Patient)",
    "type": "string",
    "req": false,
    "value": "",
    "when": [
      {
        "operator": "!=",
        "question": "monthlyContactType",
        "answerString": "Patient"
      }
    ]
  },

  "Contact Phone Numbers",
  {
    "id": "contactHomePhone",
    "t": "Home Phone",
    "type": "string",
    "req": false,
    "value": ""
  },
  {
    "id": "contactCellPhone",
    "t": "Cell Phone",
    "type": "string",
    "req": false,
    "value": ""
  },
  {
    "id": "preferredContactPhone",
    "t": "Preferred Contact Phone",
    "type": "checkbox",
    "options": ["Home Phone", "Cell Phone"],
    "req": true
  },

  {
    "id": "contactEmail",
    "t": "Email Address",
    "type": "string",
    "req": false,
    "value": ""
  }
]
    }
}

@app.post("/begin_session")
def tool_a():
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
def tool_b(data: dict[Any, Any]):
    global pageNumber
    # write information to database
    if len(formDict) == pageNumber:
        return {"message": "All information has been submitted."}
    pageNumber += 1
    return formDict[pageNumber]
