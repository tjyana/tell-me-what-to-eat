import streamlit as st
import google.generativeai as genai
from gradio_client import Client
from dotenv import load_dotenv
import os

# # for testing locally --------------------------------------
# load_dotenv()
# goog_api_key = os.getenv('GOOGLE_API_KEY') # create a variable in .env file 'GOOGLE_API_KEY' and add the api key there

# for testing on streamlit share -----------------------------
goog_api_key = st.secrets['GOOGLE_API_KEY']

def suggest_food(favorite_foods, favorite_flavors, dislikes, others):
    model = genai.GenerativeModel('gemini-1.5-flash')

    response = model.generate_content(f"""
    Favorite foods: ```{favorite_foods}```
    Favorite flavors and cuisines: ```{favorite_flavors}```
    Other considerations: ```{others}```
    Do not suggest: ``` {dislikes}```

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
    [Short summary of what's in the dish ~20 words]

    """)

    answer = response.text

    return answer

    # Last output: ```{last_output}```




def image_generator(answer):

    '''
    Generates images for recipe.

    '''

    client = Client("ByteDance/SDXL-Lightning")

    result = client.predict(
            answer, # str  in 'Enter your prompt (English)' Textbox component
            "1-Step",   # Literal['1-Step', '2-Step', '4-Step', '8-Step']  in 'Select inference steps' Dropdown component
            api_name="/generate_image_1"
    )
    file_path = result.split('gradio')[1]
    url = 'https://bytedance-sdxl-lightning.hf.space/file=/tmp/gradio' + file_path

    return url
