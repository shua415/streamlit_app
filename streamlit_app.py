import streamlit 
import pandas 

# streamlit.title("My Mom's New Healthy Diet") 
streamlit.header('Breakfast favourites')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

# reading csv text file 
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


# multi-select widget that allows users to pick fruits (widgets are index by default)
my_fruit_list = my_fruit_list.set_index('Fruit')    # set index to the column values of Fruit 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries']) #pre-populating with avo & stawbs
# put selected fruits in a variable 
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show) 


# displya fruityvice api response 
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)


