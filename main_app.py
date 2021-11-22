import streamlit as st

st.set_page_config(page_title = 'Car Price Prediction', page_icon= ':car:', layout = 'centered', initial_sidebar_state = 'auto')

import numpy as np
import pandas as pd
 
@st.cache()
def load_data() :
  df = pd.read_csv('C:/Users/Saurabh Chandra/Python_scripts/Multipage/car-prices.csv')
  df = df[['carwidth', 'enginesize', 'horsepower', 'drivewheel', 'price']]
  df['drivewheel'] = df['drivewheel'].map({'rwd' : 0,
                                           'fwd' : 1,
                                           '4wd' : 2})
  return df

car_df = load_data()  

import home
import data
import plots
import predict

page_dict = {'Home' : home, 'View Data' : data, 'Visualise Data' : plots, 'Predict' : predict}

st.sidebar.title('Navigation')
user_choice = st.sidebar.radio("Go To", tuple(page_dict.keys()))

if user_choice == 'Home' :
  home.app()

else :
  selected_page = page_dict[user_choice]
  selected_page.app(car_df)  