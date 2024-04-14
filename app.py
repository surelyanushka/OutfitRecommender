import streamlit as st
from config import api_key
import google.generativeai as genai

st.title('Outfit Recommendation App 👗')
st.subheader('Get instant Outfit Recommendations')

# User inputs
occasion = st.text_input('The occasion you want the dress for')
aesthetic = st.text_input('Choose your desired aesthetic')
weather = st.selectbox('Select the current weather', ['Sunny', 'Rainy', 'Cold', 'Snowy'])
gender = st.selectbox('Select your gender', ['Female', 'Male', 'Other'])
type_of_clothes = st.text_input('What kind of clothes are you looking for?(Shirt, pant, dress, etc?)')
color_combos = st.text_input('Type in the colours you want included')
extra = st.text_input('Additional information/requests')


prompt_enter = st.button("Outfit") 

prompt = f''' Can you create 10 outfit ideas (10 lines max) for the particular occasion,
 based on aesthetic, for the weather, the type of clothes, the colour combinations, the gender, and 
 any extra information but dont give extra info more priority over the other fields:
particular occasion:{occasion},
aesthetic:{aesthetic} ,
weather:{weather} ,
gender:{gender},
type of clothes:{type_of_clothes} ,
colour combinations:{color_combos} ,
extra iinformation:{extra} ,
If either of the instruction is not present use the best of your judgement to assume it, 
use as many fashion blogs as you want to make a decision and 
give the top 10 results bulletted in seperate lines
    Outfit :<name of the outfit>

'''

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name = "gemini-pro")


# Show stuff to the screen if there's a prompt
try:
    if prompt_enter:
        response = model.generate_content(prompt)
        st.write(response.text)
except Exception as error:
    st.write("An error has occurred", SystemExit(error))


st.write("Made with ❤️ ")