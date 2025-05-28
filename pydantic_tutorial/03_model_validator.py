from pydantic import BaseModel, EmailStr, model_validator # for validating multiple attributes of a pydantic model
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel): 

    name: str
    email: EmailStr 
    age: int
    weight: float
    married: bool
    allergies: List[str] = None
    contact_details: Dict[str, str]

    @model_validator(mode="after") # after type conversion
    def validate_emergency_contact(cls, model):  # has access to the complete model (all the fields)
        if model.age > 60 and "emergency" not in model.contact_details:
            raise ValueError("Patients older than 60 must have an emergency contact")
        return model


def insert_patient_data(patient: Patient): 

    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print("Inserted into database")

def update_patient_data(patient: Patient): 

    print(patient.name)
    print(patient.age)
    print("Updated")

patient_info = {"name": "nitish", "email": "abc@hdfc.com", "linkedin_url": "http://linkedin.com/123", "age": 65, "weight": 75.2, "married": True, "contact_details": {"phone": "3456732"}}
# below line will raise error
# patient_info = {"name": "nitish", "age": "thirty"}
patient1 = Patient(**patient_info) # step 2

insert_patient_data(patient1) # step 3

# update_patient_data(patient1)