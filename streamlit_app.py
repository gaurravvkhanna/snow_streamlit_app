import streamlit as st
import pandas as pd
st.title("Welcome to my parents diner")

st.header("Breakfast Favorites")
st.text("🥣Omega 3 & Blueberry oatmeal")
st.text("🥗Kale, Spinach & Rocket Smoothie")
st.text("🐔Hard-Boiled Free Range Egg")
st.text("🥑🍞Avocado Toast")

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
