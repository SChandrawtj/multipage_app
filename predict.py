def app(car_df) :
  st.markdown("<p style = 'color : blue; font-size : 25px'>This app uses <b> linear regression </b> to predict the price of a car based on your inputs", unsafe_allow_html = True)
  st.subheader('Select Values :')
  car_wid = st.slider('Car Width', float(car_df['carwidth'].min()), float(car_df['carwidth'].max()))
  engine_size = st.slider('Engine Size', float(car_df['enginesize'].min()), float(car_df['enginesize'].max()))
  h_power = st.slider('Horshe Power', float(car_df['horshepower'].min()), float(car_df['horshepower'].max()))
  drw_fwd = st.radio('Forward Drive wheel Car?', ('Yes', 'No'))
  if drw_fwd == 'No' :
    drw_fwd = 0
  else : 
    drw_fwd =1

  com_buick = st.radio('Is the car manufacture from buick?', ('Yes', 'No'))
  if com_buick == 'No' :
    com_buick = 0
  else :
    com_buick = 1

  if st.button('Predict') :
    st.subheader('Prediction Result : ')
    price, score, car_r2, car_mse, car_rmse, car_mae, car_msle = prection(car_df, (car_wid, engine_size, h_power, drw_fwd, com_buick))
    st.success('The predicted price of the car : dollar {:, }'.format(int(price))) 
    st.info('Accuracy score of this model is {: 2.2%}'.format(score))
    st.info(f"R squred score of this model is : {car_r2:.3f}")
    st.info(f"Mean squred error score of this model is : {car_mse:.3f}")
    st.info(f"Root mean squred error score of this model is : {car_rmse:.3f}")
    st.info(f"Mean absolute error score of this model is : {car_mae:.3f}")
    st.info(f"Mean squred log error score of this model is : {car_msle:.3f}")