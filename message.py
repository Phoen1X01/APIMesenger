from sqlalchemy import Column, Integer, Text

from database import Base





class Message(Base):
    __tablename__ = 'massages'
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False) #nullable, это про то, должен ли он быть равен нолю
