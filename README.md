# 🍳 AI Recipe Chatbot

AI Recipe Chatbot is an AI-powered chatbot that helps users generate
cooking recipes based on the ingredients they have. The chatbot uses a
Large Language Model (LLM) from the Google Gemini API to understand
natural language and generate relevant cooking instructions.

Users can ask for recipes by listing ingredients or requesting a type of
dish, and the chatbot will return:

-   Recipe name
-   Ingredients list
-   Cooking steps
-   Optional cooking tips

------------------------------------------------------------------------

# 🚀 Features

-   🤖 AI-powered chatbot using Google Gemini
-   🍳 Recipe generation from ingredients
-   💬 Natural language interaction
-   🧠 Conversation memory using Gemini chat session
-   🌐 Simple web-based interface
-   ⚡ FastAPI backend server

------------------------------------------------------------------------

# 🏗 System Architecture

User → Frontend (HTML/CSS/JS) → FastAPI Backend → Gemini API → Recipe
Response

------------------------------------------------------------------------

# 📂 Project Structure

recipe-chatbot/ │ ├── backend/ │ └── main.py │ ├── frontend/ │ ├──
index.html │ ├── style.css │ └── script.js │ └── requirements.txt

------------------------------------------------------------------------

# ⚙️ Installation

## 1. Clone the Repository

git clone https://github.com/wharwidoin/chefbot-yumyum.git cd
recipe-chatbot

## 2. Install Dependencies

pip install -r requirements.txt

Main dependencies:

-   FastAPI
-   Uvicorn
-   google-generativeai

## 3. Configure Gemini API Key

Open:

backend/main.py

Replace:

GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

with your Gemini API key from Google AI Studio.

## 4. Run the Backend Server

cd backend python -m uvicorn main:app --reload

Server will run at:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs

## 5. Run the Frontend

Open:

frontend/index.html

in your browser or use VSCode Live Server.

------------------------------------------------------------------------

# 💬 Example Usage

User Input:

"I have rice, egg, and soy sauce"

Example Response:

Recipe Name: Simple Egg Fried Rice

Ingredients: - 1 cup cooked rice - 1 egg - 1 tablespoon soy sauce - 1
clove garlic - cooking oil

Cooking Steps: 1. Heat oil in a pan. 2. Fry garlic until fragrant. 3.
Add egg and scramble it. 4. Add cooked rice and soy sauce. 5. Stir well
for 2--3 minutes.

Tips: Add green onions or chili flakes for extra flavor.

------------------------------------------------------------------------

# 🔧 AI Configuration

Model:

gemini-1.5-flash

Parameters:

temperature: 0.4--0.5\
top_p: 0.9\
max_output_tokens: 1200

------------------------------------------------------------------------

# 📚 Use Cases

-   Recipe assistant
-   Cooking inspiration tool
-   Ingredient-based meal generator
-   Beginner cooking helper

------------------------------------------------------------------------

# 🧠 AI Capabilities

The chatbot uses Natural Language Processing (NLP) to:

-   Understand ingredient-based requests
-   Generate step-by-step cooking instructions
-   Suggest cooking tips
-   Adapt responses to user prompts

------------------------------------------------------------------------

# 🔮 Future Improvements

-   AI-generated food images
-   Nutritional analysis
-   User preference memory
-   Mobile-friendly UI
-   Grocery list generation
-   Cloud deployment

------------------------------------------------------------------------

# 📜 License

This project is created for educational purposes and learning AI chatbot
development.
