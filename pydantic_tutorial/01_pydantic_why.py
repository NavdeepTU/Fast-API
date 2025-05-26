from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel): # step 1
    # define schema
    name: str # type validation
    age: int
    weight: float
    married: bool
    allergies: List[str] # List for 2 level validation
    contact_details: Dict[str, str] # Dict for 2 level validation

def insert_patient_data(patient: Patient): 

    print(patient.name)
    print(patient.age)
    print("Inserted into database")

def update_patient_data(patient: Patient): 

    print(patient.name)
    print(patient.age)
    print("Updated")

patient_info = {"name": "nitish", "age": 30, "weight": 75.2, "married": True, "allergies": ["pollen", "dust"], "contact_details": {"email": "abc@gmail.com", "phone": "3456732"}}
# below line will raise error
# patient_info = {"name": "nitish", "age": "thirty"}
patient1 = Patient(**patient_info) # step 2

insert_patient_data(patient1) # step 3

update_patient_data(patient1)