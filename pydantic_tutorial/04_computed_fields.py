from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel): 

    name: str
    email: EmailStr 
    age: int
    weight: float # kg
    height: float # mtr
    married: bool
    allergies: List[str] = None
    contact_details: Dict[str, str]

    @computed_field
    @property
    def bmi(self) -> float: # adding new field (function name) using other fields provided by the user
        bmi = round(self.weight / self.height**2, 2)
        return bmi

def insert_patient_data(patient: Patient): 

    print(patient.name)
    print(patient.age)
    print(patient.married)
    print(patient.allergies)
    print("BMI", patient.bmi)
    print("Inserted into database")

def update_patient_data(patient: Patient): 

    print(patient.name)
    print(patient.age)
    print("Updated")

patient_info = {"name": "nitish", "email": "abc@hdfc.com", "linkedin_url": "http://linkedin.com/123", "age": 30, "weight": 75.2, "height": 1.72, "married": True, "contact_details": {"phone": "3456732"}}
# below line will raise error
# patient_info = {"name": "nitish", "age": "thirty"}
patient1 = Patient(**patient_info) # step 2

insert_patient_data(patient1) # step 3

# update_patient_data(patient1)