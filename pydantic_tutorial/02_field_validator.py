from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel): 

    name: str
    email: EmailStr 
    age: int
    weight: float
    married: bool
    allergies: List[str] = None
    contact_details: Dict[str, str]

    @field_validator("email") # custom data validation
    @classmethod # remember field_validator is always a classmethod
    def email_validator(cls, value):

        valid_domains = ["hdfc.com", "icici.com"]
        # abc@gmail.com
        domain_name = value.split("@")[-1]

        if domain_name not in valid_domains:
            raise ValueError("Not a valid domain")
        
        return value
    
    @field_validator("name") # data transformation
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator("age", mode="before") # value before type coersion will come here -> by default it is after
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:
            return value
        else:
            raise ValueError("Age should be in between 0 and 100")

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

patient_info = {"name": "nitish", "email": "abc@hdfc.com", "linkedin_url": "http://linkedin.com/123", "age": 30, "weight": 75.2, "married": True, "contact_details": {"phone": "3456732"}}
# below line will raise error
# patient_info = {"name": "nitish", "age": "thirty"}
patient1 = Patient(**patient_info) # step 2

insert_patient_data(patient1) # step 3

# update_patient_data(patient1)