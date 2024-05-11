import streamlit as st
import random
import os

def main():
    st.title("Food Recommender")

    # Text input
    user_input = st.text_input("sawadee krap! what is your name:")

    # Button to trigger action
    if st.button("Submit"):
        if user_input:
            # Process user input and return a message
            message = process_input(user_input)
            st.success(message)
        else:
            st.warning("Please tell me your name.")

def process_input(input_text):
    # Example: Echo the input message
    foods = ['ข้าวมันไก่', 'ก๋วยเตี๋ยวเป็ด', 'ข้าวมันไก่', 'ข้าวหมูแดง', 'ข้าวขาหมู',
             'ข้าวหน้าเป็ด', 'ข้าวผัด', 'ข้าวขาหมู', 'ข้าวหมูกรอบ', 'ข้าวไข่เจียว',
             'ข้าวผัดกระเทียม', 'Hamasushi (not Sushiro)', 'food', 'ข้าวผัดปู',
             'ข้าวหน้าเนื้อ', 'ข้าวหมูกรอบ', 'ข้าวหมูทอด', 'ข้าวหมูสับ', 'ข้าวผัดปู',
             'khamu', 'kaki', 'katsuya', 'ice cream', 'spicy cashew nuts',
             'yayoi kusama gaaufffraeafres', 'kfc', 'kfc', 'kfc', 'kfc',
             'kfc', 'best beef', 'saenee', 'duck', 'prik nampla',
             'Hamasushi (not Sushiro)', 'Shanti', 'phet phet', 'chicken feeet',
             'cheese nan', 'cheese nan', 'cheese nan', 'sashimi bowl',
             'sashimi bowl', 'abura', 'abura', 'abura', 'abura', 'spicy nuts',
             'peeps', 'peeps', 'somtam']

    random_food = random.choice(foods)

    answer = f"""Hello Jinnichan! I knu it's you!! \n
                You should eat: \n
                {random_food}"""
    return answer

if __name__ == "__main__":
    main()
