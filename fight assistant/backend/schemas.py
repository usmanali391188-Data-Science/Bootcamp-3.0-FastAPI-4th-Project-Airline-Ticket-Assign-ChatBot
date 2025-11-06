# from pydantic import BaseModel, EmailStr
# from typing import Optional
# from pydantic import BaseModel, EmailStr

# class LeadCreate(BaseModel):
#     name: str
#     email: EmailStr
#     comment: str
#     from_city: str
#     to_city: str


# class ChatMessage(BaseModel):
#     session_id: str
#     message: str

# class ChatItem(BaseModel):
#     id: int
#     session_id: str
#     message: str
#     response: str

#     class Config:
#         from_attributes = True  # for SQLAlchemy ORM mapping

# class LeadCreate(BaseModel):
#     name: str
#     email: EmailStr
#     comment: Optional[str] = None

# class LeadOut(BaseModel):
#     id: int
#     name: str
#     email: str
#     comment: Optional[str] = None

#     class Config:
#         from_attributes = True









from pydantic import BaseModel, EmailStr
from typing import Optional

class ChatMessage(BaseModel):
    session_id: str
    message: str

class ChatItem(BaseModel):
    sender: str
    message: str

class LeadCreate(BaseModel):
    name: str
    email: EmailStr
    from_city: str
    to_city: str
    comment: Optional[str] = None
