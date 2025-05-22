from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open("patients.json", "r") as f:
        data = json.load(f)
        return data

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