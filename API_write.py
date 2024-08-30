from fastapi import FastAPI, Response, status, HTTPException, Depends
from . import models
from models import Person, Card, Account
from psycopg2.extras import RealDictCursor
import psycopg2
import time
from database import engine, get_db
from sqlalchemy.orm import Session  

models.Base.metadata.create_all(bind=engine)

# uvicorn main:app --host 127.0.0.1 --port 9999
app = FastAPI()

while True:
    try:
        conn = psycopg2.connect(host='localhost', #need to change
                                database='challenge',
                                user='postgres',
                                password="09042003", 
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("database conection was sucesfull")
        break
    except Exception as error:
        print("database conection failed")
        print("error",error)
        time.sleep(2)

#A aplicação de webhook terá como intuito receber dados criptografados de eventos de três tipos diferentes e após isso será enviado para um tópico de serviço de mensageria. A aplicação será exposta na porta :9999 e terá 3 endpoints.

@app.get('/')
def root():
    return {"Welcome to WebHook API"}

@app.get('/sqlalchemy')
def test_posts(db:Session = Depends (get_db)):
    posts = db.query(models.Post).all()
    print(posts)
    return {"data":"Successfull"}

@app.get('/account')
def get_account(db: Session = Depends(get_db)):
    account = db.query(models.Account).all()
    return account

@app.get('/account/{id}')
def get_accountid(id:int,db: Session=Depends(get_db)):
    account = db.query(models.Account).filter(models.Account.id == id).first()
    print (account)
    if not account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'account with id:{id} was not found')
    return account

@app.post('/account')
def create_account(account:Account,db:Session = Depends(get_db)):
    new_account = models.Account(**account.model_dump())
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account

@app.put('/account/{id}')
def update_account(id:int,updated_account:Account,db:Session=Depends(get_db)):
    post_query = db.query(models.Account).filter(models.Account.id == id)
    account = post_query.first()
    if account == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} does not found")
    post_query.update(updated_account.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()

@app.delete('/account/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session=Depends(get_db)):
    account = db.query(models.Account).filter(models.Account.id == id).fist()
    if account.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"post with id:{id} does not exist")
    account.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get('/person')
def get_person(db:Session=Depends(get_db)):
    person = db.query(models.Person).all()
    return person

@app.get('/person/{id}')
def get_personid(id:int,db:Session=Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.id == id).first()
    print(person)
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"person with id:{id} was not found")
    return person

@app.post('/person')
def create_person(person:Person,db:Session=Depends(get_db)):
    new_person = models.Person(**Person.model_dump())
    db.add(new_person)
    db.commit()
    db.refresh(new_person)
    return new_person

@app.put('/person/{id}')
def update_person(id:int,uptated_person:Person,db:Session=Depends(get_db)):
    post_query = db.query(models.Account).filter(models.Person.id == id)
    person = post_query.first()
    if person == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"person with id:{id} does not found")
    post_query.update(uptated_person.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()

@app.delete('/person/{id}')
def update_person(id:int,db:Session=Depends(get_db)):
    person = db.query(models.Person).filter(models.Person.id == id).first()
    if person.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"person with id:{id} does not exist")
    person.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.get('/card')
def get_card(db:Session=Depends(get_db)):
    card = db.query(models.Card).all()
    return card

@app.get('/card/{id}')
def get_cardid(id:int,db:Session=Depends(get_db)):
    card = db.query(models.Card).filter(models.Card.id == id).first()
    print(card)
    if not card:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"card with id:{id} was not found")
    return card

@app.post('/card',status_code=status.HTTP_201_CREATED)
def create_card(card:Card,db:Session=Depends(get_db)):
    new_card=models.Card(**card.model_dump())
    db.add(new_card)
    db.commit()
    db.refresh(new_card)
    return new_card

@app.put('/card/{id}')
def update_card(id:int,updated_card:Card,db:Session=Depends(get_db)):
    post_query = db.query(models.Card).filter(models.Card.id == id)
    card = post_query.first()
    if card == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"card with id:{id} does not found")
    post_query.update(updated_card.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()

@app.delete('/card/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_card(id:int,db:Session=Depends(get_db)):
    card = db.query(models.Card).filter(models.Card.id == id).first()
    if card.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"card with id:{id} does not exist")
    card.delete(synchronize_sessions=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
