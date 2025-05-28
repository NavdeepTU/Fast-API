from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal
import json

app = FastAPI()

class Patient(BaseModel):

    id: Annotated[str, Field(..., description="ID of the patient", examples=["P001"])]
    name: Annotated[str, Field(..., description="Name of the patient")]
    city: Annotated[str, Field(..., description="City where the patient is living.")]
    age: Annotated[int, Field(..., gt=0, lt=100, description="Age of the patient")]
    gender: Annotated[Literal["Male", "Female", "Others"], Field(..., description="Gender of the patient.")]
    height: Annotated[float, Field(..., gt=0, description="Height of the patient in mtrs.")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the patient in kgs.")]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / self.height**2, 2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 30:
            return "Normal"
        else:
            return "Obese"

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
        return data
    
def save_data(data):
    with open("patients.json", "w") as f:
        json.dump(data, f)

@app.get("/")  # root endpoint
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about") # about endpoint
def about():
    return {"message":"A fully functional API to manage your patient records"}

@app.get("/view") # view endpoint
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}") # endpoint to retrieve specific patient info
def view_patient(patient_id: str = Path(..., description="ID of the patient in the database", example="P001")): 
    # load all the patients
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")

@app.get("/sort")
def sort_patients(sort_by: str = Query(..., description="sort on the basis of height, weight or bmi"), order: str = Query('asc', description="sort in ascending or descending order")):

    valid_fields = ["height", "weight", "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field select from {valid_fields}")
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order select between asc and desc")
    
    data = load_data()

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=True if order == "desc" else False)

    return sorted_data

@app.post("/create")
def create_patient(patient: Patient): # data coming in the request body is directly sent to pydantic model for validation -> everything happening automatically (bmi and verdict also getting created) -> no need to manually validate the data in the function

    # load existing data
    data = load_data()

    # check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient already exist")

    # new patient add to the database
    data[patient.id] = patient.model_dump(exclude=["id"])

    # save into the json file
    save_data(data)

    return JSONResponse(status_code=201, content={"message": "patient created successfully"})