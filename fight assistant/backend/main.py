# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, EmailStr
# from fastapi.middleware.cors import CORSMiddleware
# import json
# import os

# app = FastAPI()

# # Allow frontend access
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Database file paths
# LEADS_FILE = "leads.json"
# CHATS_FILE = "chats.json"

# # Ensure files exist
# for file in [LEADS_FILE, CHATS_FILE]:
#     if not os.path.exists(file):
#         with open(file, "w") as f:
#             json.dump([], f)


# # ---- Models ----
# class ChatRequest(BaseModel):
#     session_id: str
#     message: str


# class LeadCreate(BaseModel):
#     name: str
#     email: EmailStr
#     from_city: str
#     to_city: str
#     comment: str


# # ---- Helper functions ----
# def load_json(file):
#     with open(file, "r") as f:
#         return json.load(f)


# def save_json(file, data):
#     with open(file, "w") as f:
#         json.dump(data, f, indent=4)


# # ---- Chatbot Logic ----
# @app.post("/chat")
# def chat(req: ChatRequest):
#     message = req.message.lower()
#     chats = load_json(CHATS_FILE)
#     response = ""

#     if "hi" in message or "hello" in message:
#         response = "Hello! 👋 Welcome to Flight Ticket Assistant AI. Would you like to book a flight?"
#     elif "yes" in message:
#         response = "Sure! ✈️ Please fill out the form below to book your flight."
#     elif "no" in message:
#         response = "Alright! Have a great day 😊"
#     else:
#         response = "I'm not sure I understand. Please say 'hi' to start or 'yes' to book a flight."

#     # Save chat
#     chats.append({
#         "session_id": req.session_id,
#         "message": req.message,
#         "response": response
#     })
#     save_json(CHATS_FILE, chats)

#     return {"response": response}


# # ---- Lead Form ----
# @app.post("/lead")
# def create_lead(lead: LeadCreate):
#     leads = load_json(LEADS_FILE)
#     leads.append(lead.dict())
#     save_json(LEADS_FILE, leads)
#     return {"message": "Lead saved successfully"}






# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, EmailStr
# from fastapi.middleware.cors import CORSMiddleware
# import json
# import os

# app = FastAPI()

# # Allow frontend access
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Database file paths
# LEADS_FILE = "leads.json"
# CHATS_FILE = "chats.json"

# # Ensure files exist
# for file in [LEADS_FILE, CHATS_FILE]:
#     if not os.path.exists(file):
#         with open(file, "w") as f:
#             json.dump([], f)


# # ---- Models ----
# class ChatRequest(BaseModel):
#     session_id: str
#     message: str


# class LeadCreate(BaseModel):
#     name: str
#     email: EmailStr
#     from_city: str
#     to_city: str
#     comment: str


# # ---- Helper functions ----
# def load_json(file):
#     with open(file, "r") as f:
#         return json.load(f)


# def save_json(file, data):
#     with open(file, "w") as f:
#         json.dump(data, f, indent=4)


# # ---- Chatbot Logic ----
# @app.post("/chat")
# def chat(req: ChatRequest):
#     message = req.message.lower()
#     chats = load_json(CHATS_FILE)
#     response = ""

#     # --- Simple Q&A rules ---
#     if "hi" in message or "hello" in message:
#         response = "Hello! 👋 Welcome to Flight Ticket Assistant AI. Would you like to book a flight?"
#     elif "yes" in message or "sure" in message or "yea" in message:
#         response = "Sure! ✈️ Please fill out the form below to book your flight."
#     elif "no" in message:
#         response = "Alright! Have a great day 😊"
#     elif "price" in message or "cost" in message:
#         response = "💰 The flight price is around $79 depending on the route and time!"
#     elif "from" in message and "to" in message:
#         response = "Got it! I’ll check available flights between those cities. Please fill out the form for more details."
#     else:
#         response = "I'm not sure I understand. Please say 'hi' to start or 'yes' to book a flight."

#     # Save chat
#     chats.append({
#         "session_id": req.session_id,
#         "message": req.message,
#         "response": response
#     })
#     save_json(CHATS_FILE, chats)

#     return {"response": response}


# # ---- Lead Form ----
# @app.post("/lead")
# def create_lead(lead: LeadCreate):
#     leads = load_json(LEADS_FILE)
#     leads.append(lead.dict())
#     save_json(LEADS_FILE, leads)
#     return {"message": "Lead saved successfully"}












# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel, EmailStr
# import sqlite3
# import os
# from gemini_client import generate_reply

# app = FastAPI()

# DB_PATH = "chat.db"
# LEADS_DB = "leads.db"

# class ChatRequest(BaseModel):
#     session_id: str
#     message: str

# class Lead(BaseModel):
#     name: str
#     email: EmailStr
#     from_city: str
#     to_city: str
#     comment: str | None = None


# # ----------- Database setup -----------
# def init_db():
#     with sqlite3.connect(DB_PATH) as conn:
#         conn.execute(
#             """CREATE TABLE IF NOT EXISTS chats (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 session_id TEXT,
#                 role TEXT,
#                 message TEXT
#             )"""
#         )

#     with sqlite3.connect(LEADS_DB) as conn:
#         conn.execute(
#             """CREATE TABLE IF NOT EXISTS leads (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT,
#                 email TEXT,
#                 from_city TEXT,
#                 to_city TEXT,
#                 comment TEXT
#             )"""
#         )

# init_db()


# # ----------- Helper for saving chat -----------
# def save_chat(session_id, role, message):
#     with sqlite3.connect(DB_PATH) as conn:
#         conn.execute(
#             "INSERT INTO chats (session_id, role, message) VALUES (?, ?, ?)",
#             (session_id, role, message),
#         )


# # ----------- Custom Responses (Independent Logic) -----------
# CUSTOM_RESPONSES = {
#     "hi": "👋 Hello! Welcome to Flight Ticket Assistant AI. Would you like to book a flight?",
#     "hello": "👋 Hey there! I'm your Flight Assistant. Want to book a ticket?",
#     "yes": "Great! Please fill in your name, email, and cities in the form above.",
#     "what will the price of this flight": "💸 It will cost around $79, depending on the destination.",
#     "bye": "Goodbye! 👋 Have a safe journey!",
# }


# @app.post("/chat")
# async def chat(request: ChatRequest):
#     user_msg = request.message.strip().lower()
#     save_chat(request.session_id, "user", request.message)

#     # --- Check for predefined response first ---
#     for key, response in CUSTOM_RESPONSES.items():
#         if key in user_msg:
#             bot_reply = response
#             save_chat(request.session_id, "assistant", bot_reply)
#             return {"reply": bot_reply}

#     # --- If not matched, fallback to LLM ---
#     try:
#         bot_reply = generate_reply(user_msg)
#         save_chat(request.session_id, "assistant", bot_reply)
#         return {"reply": bot_reply}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error generating reply: {e}")


# @app.post("/lead")
# async def save_lead(lead: Lead):
#     with sqlite3.connect(LEADS_DB) as conn:
#         conn.execute(
#             "INSERT INTO leads (name, email, from_city, to_city, comment) VALUES (?, ?, ?, ?, ?)",
#             (lead.name, lead.email, lead.from_city, lead.to_city, lead.comment),
#         )
#     return {"message": "Lead saved successfully!"}












from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import init_db, SessionLocal, Chat, Lead
from schemas import ChatMessage, LeadCreate
from gemini_client import generate_reply

app = FastAPI()
init_db()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
def chat(message: ChatMessage):
    db = SessionLocal()
    try:
        chat_entry = Chat(session_id=message.session_id, sender="user", message=message.message)
        db.add(chat_entry)
        db.commit()

        reply = generate_reply(message.message)
        bot_entry = Chat(session_id=message.session_id, sender="bot", message=reply)
        db.add(bot_entry)
        db.commit()

        return {"response": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

@app.post("/lead")
def create_lead(lead: LeadCreate):
    db = SessionLocal()
    try:
        new_lead = Lead(**lead.model_dump())
        db.add(new_lead)
        db.commit()
        return {"message": "Lead saved successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()
