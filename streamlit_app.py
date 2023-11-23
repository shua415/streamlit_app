import streamlit 
import pandas 
import requests
import snowflake.connector
from urllib.error import URLError 

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

# FUNCTION that returns the info of the requested fruit choice 
def get_fruityvice_data(this_fruit_choice): 
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    # normalises the data by applying a standard format to the table 
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized 

# displya fruityvice api response 
streamlit.header("Fruityvice Fruit Advice!")
try: 
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice: 
    streamlit.error("Please select a fruit to get information.") 
  else: 
    back_from_function = get_fruityvice_data(fruit_choice) 
    # displays the normalised fruityvice data 
    streamlit.dataframe(back_from_function)
    
except URLError as e: 
  streamlit.error()

# don't run anything past here 
streamlit.header("The fruit load list contains:")
# Snowflake-related functions 
def get_fruit_load_list(): 
  with my_cnx.cursor() as my_cur: 
    my_cur.execute("select * from fruit_load_list") 
    return my_cur.fetchall() 

# add a button to load the fruit 
if streamlit.button('Get Fruit Load List'): 
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])  
  my_data_rows = get_fruit_load_list() 
  streamlit.dataframe(my_data_rows) 
# my_cur = my_cnx.cursor()
# my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
# my_data_rows = my_cur.fetchall()

# allows user to add fruit 
add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')") 
