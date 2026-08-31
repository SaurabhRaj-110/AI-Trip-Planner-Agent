import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from agent.prompts import SYSTEM_PROMPT
from tools.trip_tool import calculate_optimal_itinerary

load_dotenv()

class Agent:
    def __init__(self):
        # Initialize the new genai client
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        
        # Create a persistent chat session with automatic function execution
        self.chat = self.client.chats.create(
            model="gemini-3.6-flash",  # Latest Flash model (high quota, fast)
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                tools=[calculate_optimal_itinerary],
                temperature=0.0
            )
        )

    def chat_with_user(self, user_input: str) -> str:
        # send_message intercepts tool requests, runs calculate_optimal_itinerary locally, 
        # and returns the final formulated response automatically.
        response = self.chat.send_message(user_input)
        return response.text