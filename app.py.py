import streamlit as st
import random

st.title("🎮 Guess the Number")

if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 10)

guess = st.number_input("Guess a number (1–10)", 1, 10)

if st.button("Check"):
    if guess == st.session_state.number:
        st.success("Correct! 🎉")
    else:
        st.error("Wrong 😢 Try again")
