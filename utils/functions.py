import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# for testing locally --------------------------------------
load_dotenv()
goog_api_key = os.getenv('GOOGLE_API_KEY') # create a variable in .env file 'GOOGLE_API_KEY' and add the api key there

# # for testing on streamlit share -----------------------------
# goog_api_key = st.secrets['GOOGLE_API_KEY']

def suggest_food(favorite_foods, favorite_flavors, favorite_cuisines, dislikes, recent_meals):
    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(f"""
    Favorite foods: ```{favorite_foods}```
    Favorite flavors: ```{favorite_flavors}```
    Favorite cuisines: ```{favorite_cuisines}```
    Dislikes: ```{dislikes}```
    Recent meals: ```{recent_meals}```
    Given the above information, please analyze this person's favorite foods, flavors, and cuisines.
    Based on this, provide a recommendation for a meal that they would enjoy.
    Please also consider their recent meals and things they don't like, and avoid suggesting those.
    If they provide limited information, please try to extrapolate flavor profile of that dish,
    and recommend foods with similar profiles from other cuisines.
    (eg. If they say their favorite dish is somtam, please don't suggest somtam,
    but suggest a dishes from non-Thai cuisines with spicy/sour/salty/fishy flavors,
    like oi muchim or spicy tuna).
    If you're going to suggest a Thai food, please be very specific and provide
    the Thai name of the recipe (please don't say Spicy Thai soup, Thai curry, etc).
    If inputs don't make sense, it might be a Thai word spelled out in English.

    Output should be the name of the dish, followed by a short summary (~20 words) of what's in the dish.
    Output format:

    [Name of the dish]
    [Short summary of what's in the dish]
    """)

    answer = response.text

    return answer
