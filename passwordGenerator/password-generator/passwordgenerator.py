import streamlit as st
import random
import string

def generate_password(Length,use_digits,use_special):
    characters= string.ascii_letters
    if use_digits:
        characters+=string.digits

    if use_special:
        characters+=string.punctuation

    return ' '.join(random.choice(characters) for _ in range(Length))

st.title("Password Generator")
Length= st.slider("Select Password Length" , min_value=6 , max_value=20, value=12)
use_digits=st.checkbox("Include Digits")
use_special=st.checkbox("Include special characters")

if st.button("Generate Password"):
    password=generate_password(Length,use_digits,use_special)
    st.write(f"Generated password {password}")
st.write("------------------")
st.write("Build with ❤ by syeda maham amjad")
