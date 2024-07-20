import streamlit as st
from utils.functions import suggest_food, image_generator
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



if 'last_output' not in st.session_state:
    st.session_state.last_output = None

def main():
    # Title
    st.sidebar.title("Food Recommender")
    st.sidebar.write("Hello! Please tell me your preferences:")

    # Input fields
    favorite_foods = st.sidebar.text_input("Favorite foods")
    favorite_flavors = st.sidebar.text_input("Favorite flavors or cuisines")
    dislikes = st.sidebar.text_input("Want to avoid (dislikes, allergies, recent meals)")
    others = st.sidebar.text_input("Other considerations (optional)")

    # Submit button
    if st.sidebar.button("Submit"):
        # Process the inputs
        st.session_state.favorite_foods = favorite_foods
        st.session_state.favorite_flavors = favorite_flavors
        st.session_state.dislikes = dislikes
        st.session_state.others = others

        st.header("You should eat...")

        output = suggest_food(favorite_foods, favorite_flavors, dislikes, others)


        # output = suggest_food(favorite_foods, favorite_flavors, dislikes, others, last_output)


        url = image_generator(output)

        # add func to keep last output from showing
        # st.session_state.last_output = output.split("\n")[-2]

        process_inputs(output, url)



def process_inputs(input1, url):
    # Function to display the final output
    # Process the inputs here
    st.write(" ", input1)
    st.image(url, use_column_width=True)


if __name__ == "__main__":
    main()
