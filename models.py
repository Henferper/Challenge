from database import Base
from sqlalchemy import Column, Integer,DateTime, Date, String, Float

class Person(Base):
    __tablename__ = "person"

    datetime = Column(DateTime,primary_key=False,nullable=False)
    body = Column(String,primary_key=False,nullable=False)
    event = Column(String,primary_key=False,nullable=False)
    person_id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String,primary_key=False,nullable=False)
    email = Column(String,primary_key=False,nullable=False)
    gender = Column(String,primary_key=False,nullable=False)
    birth_date = Column(Date,primary_key=False,nullable=False)
    salary = Column(Float,primary_key=False,nullable=False)
    cpf = Column(String,primary_key=False,nullable=False)
    
class Account(Base):
    __tablename__ = "account"
    datetime = Column(DateTime,primary_key=False,nullable=False)
    body = Column(String,primary_key=False,nullable=False)
    event = Column(String,primary_key=False,nullable=False)
    account_id = Column(Integer,primary_key=True,nullable=False)
    status_id = Column(Integer,primary_key=False,nullable=False)
    due_day = Column(Integer,primary_key=False,nullable=False)
    person_id = Column(Integer,primary_key=False,nullable=False)
    balance = Column(Float,primary_key=False,nullable=False)
    avaliable_balance = Column(Float,primary_key=False)

class Card(Base):
    __tablename__ = "card"
    datetime = Column(DateTime,primary_key=False,nullable=False)
    body = Column(String,primary_key=False,nullable=False)
    event = Column(String,primary_key=False,nullable=False)
    card_id = Column(Integer,primary_key=True,nullable=False)
    card_number = Column(String,primary_key=False,nullable=False)
    account_id = Column(String,primary_key=False,nullable=False)
    status_id = Column(String,primary_key=False,nullable=False)
    limit = Column(Float,primary_key=False,nullable=False)
    expiration_date = Column(String,primary_key=False)