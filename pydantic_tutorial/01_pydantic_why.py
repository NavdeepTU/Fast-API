from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel): # step 1
    # define schema
    name: Annotated[str, Field(max_length=50, title="Name of the patient", description="Give the name of the patient in less than 50 characters", examples=["Nitish", "Amit"])] # Field function allows custom validation and also allows to attach metadata -> Field function is used in combination with Annotated
    # name: str = Field(max_length=50) # type validation using str, length should not ne greater than 50 characters
    email: EmailStr # EmailStr for automatic data validation
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120) # custom data validation -> setting range
    weight: Annotated[float, Field(gt=0, strict=True)] # strict = True will not allow to type coerce eg - will not allow "75.2" to convert to float automatically
    # married: bool = False # default value False
    married: Annotated[bool, Field(default=None, description="Is the patient married or not.")] # can also set default values using Field function
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length= 5)] # List for 2 level validation, No more than 5 allergies
    contact_details: Dict[str, str] # Dict for 2 level validation

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

patient_info = {"name": "nitish", "email": "abc@gmail.com", "linkedin_url": "http://linkedin.com/123", "age": 30, "weight": 75.2, "married": True, "contact_details": {"phone": "3456732"}}
# below line will raise error
# patient_info = {"name": "nitish", "age": "thirty"}
patient1 = Patient(**patient_info) # step 2

insert_patient_data(patient1) # step 3

# update_patient_data(patient1)