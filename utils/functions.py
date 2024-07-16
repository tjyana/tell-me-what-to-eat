import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# # for testing locally --------------------------------------
# load_dotenv()
# goog_api_key = os.getenv('GOOGLE_API_KEY') # create a variable in .env file 'GOOGLE_API_KEY' and add the api key there

# for testing on streamlit share -----------------------------
goog_api_key = st.secrets['GOOGLE_API_KEY']

def suggest_food(favorite_foods, favorite_flavors, favorite_cuisines, dont_want_to_eat, recent_meals):
    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(f"""
    Favorite foods: ```{favorite_foods}```
    Favorite flavors: ```{favorite_flavors}```
    Favorite cuisines: ```{favorite_cuisines}```
    Don't want to eat: ```{dont_want_to_eat}```
    Recent meals: ```{recent_meals}```
    Given the above information, please analyze this person's favorite foods
    and recent meals and provide a recommendation for a meal that they would enjoy.
    Output should be a single word or phrase.
    """)

    answer = response.text

    return answer
