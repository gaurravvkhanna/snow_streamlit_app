import streamlit as st
import pandas as pd
import requests
import snowflake.connector
from urllib.error import URLError

def get_fruityvice_data(fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
  return fruityvice_normalized


st.title("Welcome to my parents diner")

st.header("Breakfast Favorites")
st.text("🥣Omega 3 & Blueberry oatmeal")
st.text("🥗Kale, Spinach & Rocket Smoothie")
st.text("🐔Hard-Boiled Free Range Egg")
st.text("🥑🍞Avocado Toast")

st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
st.dataframe(fruits_to_show)

st.header("Fruityvice Fruit Advice!")

try:
  fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
  if not fruit_choice:
    st.error("you need to enter a fruit")
  else:  
    st.dataframe(get_fruityvice_data(fruit_choice))
except URLError as e:
  st.error()

st.stop()
#Get snowflake details
my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
st.text("Hello from Snowflake:")
st.dataframe(my_data_rows)

second_fruit = st.text_input('Add your fruit of choice to the list')
my_cur.execute(f"insert into fruit_load_list values ('{second_fruit}')")
