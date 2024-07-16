import streamlit as st
from utils.functions import suggest_food
import random
import os

# def main():
#     st.title("Food Recommender")

#     # Text input
#     user_input = st.text_input("sawadee krap! what is your name:")

#     # Button to trigger action
#     if st.button("Submit"):
#         if user_input:
#             # Process user input and return a message
#             message = process_input(user_input)
#             st.success(message)
#         else:
#             st.warning("Please tell me your name.")

# def process_input(input_text):
#     # Example: Echo the input message
#     foods = ['ข้าวมันไก่', 'ก๋วยเตี๋ยวเป็ด', 'ข้าวมันไก่', 'ข้าวหมูแดง', 'ข้าวขาหมู',
#              'ข้าวหน้าเป็ด', 'ข้าวผัด', 'ข้าวขาหมู', 'ข้าวหมูกรอบ', 'ข้าวไข่เจียว',
#              'ข้าวผัดกระเทียม', 'Hamasushi (not Sushiro)', 'food', 'ข้าวผัดปู',
#              'ข้าวหน้าเนื้อ', 'ข้าวหมูกรอบ', 'ข้าวหมูทอด', 'ข้าวหมูสับ', 'ข้าวผัดปู',
#              'khamu', 'kaki', 'katsuya', 'ice cream', 'spicy cashew nuts',
#              'yayoi kusama gaaufffraeafres', 'kfc', 'kfc', 'kfc', 'kfc',
#              'kfc', 'best beef', 'saenee', 'duck', 'prik nampla',
#              'Hamasushi (not Sushiro)', 'Shanti', 'phet phet', 'chicken feeet',
#              'cheese nan', 'cheese nan', 'cheese nan', 'sashimi bowl',
#              'sashimi bowl', 'abura', 'abura', 'abura', 'abura', 'spicy nuts',
#              'peeps', 'peeps', 'somtam']

#     random_food = random.choice(foods)

#     makyu = ['jinnichan', 'makyu', 'jin']

#     if input_text.lower() in makyu:
#         answer = f"""Hello makyu! I knu it's you!! \n
#                 You should eat: \n
#                 {random_food}"""
#         return answer
#     else:
#         answer =  f"Hello {input_text}! You should eat: {random_food}"
#         return answer


# if __name__ == "__main__":
#     main()



def main():
    # Title
    st.sidebar.title("Food Recommender")
    st.sidebar.write("Sawadee khrap! Please tell me your preferences:")

    # Input fields
    favorite_foods = st.sidebar.text_area("Favorite foods", height=100)
    favorite_flavors = st.sidebar.text_area("Favorite flavors", height=100)
    favorite_cuisines = st.sidebar.text_area("Favorite cuisines", height=100)
    dont_want_to_eat = st.sidebar.text_area("Don't want to eat", height=100)
    recent_meals = st.sidebar.text_area("Recent meals", height=100)

    # Submit button
    if st.sidebar.button("Submit"):
        # Process the inputs
        st.session_state.favorite_foods = favorite_foods
        st.session_state.favorite_flavors = favorite_flavors
        st.session_state.favorite_cuisines = favorite_cuisines
        st.session_state.dont_want_to_eat = dont_want_to_eat
        st.session_state.recent_meals = recent_meals

        st.header("You should eat...")
        output = suggest_food(favorite_foods, favorite_flavors, favorite_cuisines, dont_want_to_eat, recent_meals)
        process_inputs(output)


def process_inputs(input1):
    # Function to display the final output
    # Process the inputs here
    st.title(" ", input1)


if __name__ == "__main__":
    main()
