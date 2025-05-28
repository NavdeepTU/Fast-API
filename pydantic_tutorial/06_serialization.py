from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str = "Male"
    age: int
    address: Address

address_dict = {"city": "gurgaon", "state": "haryana", "pin": "122001"}

address1 = Address(**address_dict)

patient_dict = {"name": "nitish", "age": 35, "address": address1}

patient1 = Patient(**patient_dict)

temp = patient1.model_dump() # convert existing pydantic model to a python dictionary

print(temp) 
# {'name': 'nitish', 'gender': 'male', 'age': 35, 'address': {'city': 'gurgaon', 'state': 'haryana', 'pin': '122001'}}
print(type(temp)) # <class 'dict'>

temp1 = patient1.model_dump(include=["name", "gender"]) # only include name and gender field in the dictionary
print(temp1)

temp1 = patient1.model_dump(exclude=["name", "gender"]) # exclude name and gender fields from all the fields
print(temp1)

temp1 = patient1.model_dump(exclude={"address": ["state"]}) # exclude state from address nested model
print(temp1)

temp1 = patient1.model_dump(exclude_unset=True) # exclude fields that are not provided(do not add use default values)
print(temp1)

temp = patient1.model_dump_json() # convert existing pydantic model to a python str -> can export to json then

print(temp) 
# {"name":"nitish","gender":"male","age":35,"address":{"city":"gurgaon","state":"haryana","pin":"122001"}}
print(type(temp)) # <class 'str'>