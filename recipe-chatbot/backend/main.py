from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai

# =========================
# GEMINI CONFIG
# =========================

GEMINI_API_KEY = "xxxxxxxxxxxxxxxxxx"

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(
    "gemini-2.5-flash",
    system_instruction="""
You are a friendly AI Recipe Assistant.

Your job is to help users cook meals from ingredients they have.

Always answer using this structure:

Recipe Name: <name>

Ingredients:
- ingredient
- ingredient
- ingredient

Cooking Steps:
1. step
2. step
3. step
4. step

Tips:
Optional cooking tips.

Rules:
- Keep the language simple
- Always include ingredients and steps
- If the user gives ingredients, create a recipe using them
"""
)

# create chat session (keeps conversation memory)
chat_session = model.start_chat(history=[])

# =========================
# FASTAPI SETUP
# =========================

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# REQUEST MODEL
# =========================

class ChatRequest(BaseModel):
    message: str


# =========================
# ROOT ENDPOINT
# =========================

@app.get("/")
def home():
    return {"message": "AI Recipe Chatbot API is running 🍳"}


# =========================
# CHAT ENDPOINT
# =========================

@app.post("/chat")
async def chat(req: ChatRequest):

    user_message = req.message

    try:
        response = chat_session.send_message(
            user_message,
            generation_config={
                "temperature": 0.4,
                "top_p": 0.9,
                "max_output_tokens": 2000
            }
        )

        reply = response.text

    except Exception as e:
        reply = "Sorry, I couldn't generate a recipe right now."

    return {"response": reply}