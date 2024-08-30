from pydantic import BaseModel
from datetime import datetime,date

class Information_Body(BaseModel):
    time:datetime
    body:str
    event:str

class Person(BaseModel):
    person_id:int
    name:str
    email:str
    gender:str
    birth_date:date
    address:str
    salary:float
    cpf:str

    class Config:
        form_attributes = True

class Account(BaseModel):
    account_id:int
    status_id:int
    due_day:int
    person_id:int
    balance:float
    avaliable_balance:float

    class Config:
        form_attributes = True

class Card(BaseModel):
    card_id:int
    card_number:str
    account_id:int
    status_id:int
    limit:float
    expiration_date:str

    # Verify if any posts are dict with the responses
    class Config:
        form_attributes = True