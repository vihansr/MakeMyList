from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List

import os
from dotenv import load_dotenv

import json

# Load environment variables
dotenv_path = os.path.join(os.getcwd(), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path=dotenv_path)
else:
    load_dotenv()

class ItemList(BaseModel):
    name: str = Field(description="Name of the item.")
    quantity: str = Field(description="Quantity of the item, including units. Use 'Depends on the event...' if unsure") 
    price: str = Field(description="Average Price of the item, in Indian Rupees.")

class MakeMyList(BaseModel):
    title: str = Field(description="Title of the order to be placed, derived from the items and their type. Max 4 words.")
    items: List[ItemList]

# Lazy client instantiation to prevent crash at startup if key is missing
client = None

def get_client():
    global client
    if client is None:
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is not set. Please create a .env file with your key.")
        client = genai.Client(api_key=api_key)
    return client

SYSTEM_PROMPT = """
You are an expert event planner and logistics specialist. Your goal is to create a complete, well-thought-out list of items required for any event based on the user's description.

Ensure you follow these rules:
1. **Completeness**: Include all categories of items necessary for the event type (e.g., food, beverages, snacks, tableware/disposables, and any other essentials). Never leave critical items out.
2. **Realistic Quantities**: Calculate quantities precisely based on the number of attendees, duration, and type of event. Make sure quantities are descriptive (e.g., "3 Bottles of 1.25L", "2 kg", "12 units").
3. **Accurate Budgeting**: Estimate average prices in Indian Rupees (INR) based on current local market rates in India. Return the price as a number or simple string (e.g. "350", "1200") without currency symbols, unless requested otherwise.
4. **Specific Names**: Avoid generic items like "Drinks" or "Food". Be specific, e.g., "Coca-Cola / Sprite (1.25L)", "Paneer Tikka (8 pcs per portion)".
5. **Creative & Concise Title**: Create a concise, professional title (max 4 words) for the list that encapsulates the event type.
"""

def get_list(user_prompt):
    cl = get_client()
    
    response = cl.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            response_mime_type="application/json",
            response_schema=MakeMyList,
        ),
    )

    result = MakeMyList.model_validate_json(response.text)
    # Return as a parsed python dictionary so app.py and templates can use it directly
    return result.model_dump()


