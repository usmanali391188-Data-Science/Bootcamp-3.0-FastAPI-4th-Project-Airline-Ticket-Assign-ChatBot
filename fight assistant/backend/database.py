# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import os
# from dotenv import load_dotenv

# load_dotenv()

# DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./chatbot.db")

# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()



from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

Base = declarative_base()


class Chat(Base):
    __tablename__ = 'chats'
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, index=True)
    sender = Column(String)
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Lead(Base):
    __tablename__ = 'leads'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    from_city = Column(String)
    to_city = Column(String)
    comment = Column(Text)


chat_engine = create_engine("sqlite:///chat.db", connect_args={"check_same_thread": False})
lead_engine = create_engine("sqlite:///leads.db", connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=chat_engine)

def init_db():
    Base.metadata.create_all(bind=chat_engine)
    Base.metadata.create_all(bind=lead_engine)
