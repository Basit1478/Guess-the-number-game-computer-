import streamlit as st
import random

st.title("Guess the Number Game (Computer)")

if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randint(1, 100)
    st.session_state.attempts = 0

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.attempts += 1
    if guess < st.session_state.number_to_guess:
        st.warning("Too low! Try again.")
    elif guess > st.session_state.number_to_guess:
        st.warning("Too high! Try again.")
    else:
        st.success(f"Congratulations! You guessed the number {st.session_state.number_to_guess} in {st.session_state.attempts} attempts.")
        st.session_state.number_to_guess = random.randint(1, 100)
        st.session_state.attempts = 0