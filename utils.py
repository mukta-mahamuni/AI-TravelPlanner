import os
import google.generativeai as genai
from langchain.memory import ConversationBufferMemory
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage
import config

genai.configure(api_key=config.GOOGLE_GENAI_API_KEY)

memory = ConversationBufferMemory(memory_key="chat_history")

def fetch_real_time_travel_data(source, destination):
    """
    Mock function to simulate real-time travel data fetching
    """
    travel_data = {
        "train": "Rs.1200 (Express Train, 6 hours)",
        "bus": "Rs.800 (AC Bus, 8 hours)",
        "flight": "Rs.5000 (Economy, 1.5 hours)",
        "cab": "Rs.7000 (Private Taxi, 10 hours)"
    }

    return f"Travel options from {source} to {destination}: {travel_data}"

def get_travel_recommendations(source, destination):
    """
    Uses Google GenAI within LangChain to generate travel recommendations.
    """
    prompt = f"""
    Provide the best travel options from {source} to {destination}.
    Consider cab, train, bus, and flights.
    Include estimated costs and travel durations.
    """

    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", google_api_key=config.GOOGLE_GENAI_API_KEY)

    response = llm.predict(prompt)

    return response