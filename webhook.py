from fastapi import FastAPI,status
from util import generate_private_key,function_descrypted_message
from schemas import Person
import models
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO) 

@app.get('/')
def root(): 
    return {"data":"API WebHook"}

@app.post('/person', status_code=status.HTTP_201_CREATED, response_model=None)
def post_person(person: Person):
    private_key = generate_private_key()
    message_dict = function_descrypted_message(person, private_key)
    new_person = models.Person(**message_dict)
    logging.info("Private key:",private_key)
    logging.info("Message dict",message_dict)
    logging.info("New person",new_person)
    return new_person

@app.post('/account',status_code=status.HTTP_201_CREATED)
def post_account():
    return

@app.post('/card',status_code=status.HTTP_201_CREATED)
def post_card():
    return