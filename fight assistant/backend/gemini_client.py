# import os
# import requests
# from dotenv import load_dotenv

# load_dotenv()

# API_KEY = os.getenv("GEMINI_API_KEY")
# MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")

# def generate_reply(prompt: str) -> str:
#     """
#     Sends a prompt to Gemini API and returns the model's reply.
#     """
#     if not API_KEY:
#         return "Error: Missing GEMINI_API_KEY."

#     try:
#         url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"

#         payload = {
#             "contents": [{"parts": [{"text": prompt}]}]
#         }

#         response = requests.post(url, json=payload, timeout=10)
#         data = response.json()

#         return (
#             data.get("candidates", [{}])[0]
#             .get("content", {})
#             .get("parts", [{}])[0]
#             .get("text", "No response from Gemini API.")
#         )

#     except Exception as e:
#         return f"Error: {str(e)}"



def generate_reply(prompt: str) -> str:
   
    responses = {
        "hi": "👋 Hello! Welcome to Flight Ticket Assistant AI. Would you like to book a flight?",
        "yes": "Great! Please tell me your departure and destination cities.",
        "what will the price of this flight": "It will cost around $79 depending on the airline.",
        "thank you": "You're very welcome! 😊"
    }

    prompt_lower = prompt.lower()
    for key, response in responses.items():
        if key in prompt_lower:
            return response

    return "I'm not sure, but I can help you find flights or information about your trip."
