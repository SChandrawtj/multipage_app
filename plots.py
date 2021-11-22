import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def app(car_df) :
  st.header('Visualise Data')
  st.set_option('deprecation.showPyplotGlobalUse', False)
  st.subheader('Scatterplot')
  feat_list = st.multiselect('Select the x-axis values', ('carwidth', 'enginesize', 'horshepower', 'drivewheel', 'car_company_buick'))
  for feat in feat_list :
    st.subheader(f"Scatter Plot between {feat} and Price")
    plt.figure(figsize= (12, 6))
    sns.scatterplot(x = feat, y = 'price', data = car_df)
    st.pyplot()

  st.subheader('Visualisation Selector')
  plot_types = st.multiselect('Select charts/Plots', ('Histogram', 'Box Plot', 'Corrrelation Heatmap'))
  if 'Histogram' in plot_types :
    st.subheader('Histogram')
    columns = st.selectbox('Select the column to creat its histogram', ('carwidth', 'enginesize', 'horshepower'))
    plt.figure(figsize = (18, 8))
    plt.title(f"Histogram for {columns}")
    plt.hist(x = car_df[columns], bins = 'sturges', edgecolor = 'black')
    st.pyplot()

  if 'Box Plot' in plot_types :
    st.subheader('Box Plot')
    columns = st.selectbox('Select the column to creat its histogram', ('carwidth', 'enginesize', 'horshepower')
    plt.figure(figsize = (18, 8))
    plt.title(f"Box plot for {columns}")
    sns.boxplot(car_df[columns])
    st.pyplot()

  if 'Correlation Heatmap' in plot_types :
    st.subheader('Correlation Heatmap')
    plt.figure(figsize = (12, 8), dpi = 90)
    ax = sns.heatmap(car_df.corr(), annot = True)
    bottom, top = ax.get_ylim()
    ax.set_ylim(bottom + 0.5, top - 0.5)
    st.pyplot() 