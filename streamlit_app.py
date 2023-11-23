import streamlit 
import pandas 
import requests
import snowflake.connector

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

# displya fruityvice api response 
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")  # gets data from the website 

# normalises the data by applying a standard format to the table 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# displays the normalised fruityvice data 
streamlit.dataframe(fruityvice_normalized)



my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("The fruit load list contains:")
streamlit.text(my_data_row)
