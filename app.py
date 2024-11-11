from fastapi import FastAPI
from fastapi.params import Depends
from sqlalchemy.orm import Session

from database import Base, engine, session_factory
from dto import MessageCreate
from message import Message
from pydantic import BaseModel

app = FastAPI()


def get_db():
    db = session_factory() #создаем ноую сессию
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index(db: Session = Depends(get_db)):
    messages = db.query(Message).order_by(Message.id).all() #запросили и получили все элементы

    messages_text = []
    for message in messages:
        messages_text.append(message.text)

    return messages_text

@app.post("/")
def add(message_create: MessageCreate, db: Session = Depends(get_db)):
    message = Message(text=message_create.text)
    db.add(message)
    db.commit()
    return ""



Base.metadata.create_all(bind=engine) #мы обращаемся к базе и просим создать все таблицы унаследованные от Base, bind=engine, это обращение к созданному движку
