import pandas as pd
import numpy as np
import streamlit as st
#from streamlit_option_menu import option_menu
from PIL import Image

#read csv without changing the dtypes

def read_csv_o2o(path):
    dtypes = {
    'User_id':np.int32,
    'Coupon_id':np.int32,}
    return pd.read_csv(path, dtype=dtypes)

def read_csv_pred(path):
    dtypes = {
    'User_id':np.int32,'Probability':np.float64,
    'Coupon_id':np.int32}
    return pd.read_csv(path, dtype=dtypes)

o2olist = read_csv_o2o('o2o_list.csv')
pred = read_csv_pred('submit_final.csv')
#streamlit code start--

st.header('🛍️O2O Coupon Redemption')

target = st.text_input("Please input customer id:")
submitted = st.button('Submit')
if not submitted:
    banner = Image.open('banner.jpeg')
    st.image('banner.jpeg', width=700)
    st.markdown('###')
    

if submitted:
    user_df=o2olist[o2olist['User_id']==int(target)]
    pred_df=pred[pred['User_id']==int(target)]
    #user_df.fillna(0,inplace=True)

    no_coupon=len(user_df.index)
    user=user_df.loc[user_df['User_id'] == int(target), 'User_id'].iloc[0]
    st.write("User id",user, "received",no_coupon,"coupons.")

    pred_df['Probability']=pd.Series(["{0:.2f}%".format(val * 100) for val in pred_df['Probability']], index = pred_df.index)
    pred_df.drop(columns='User_id',axis=1,inplace=True)
    pred_df.drop(columns='Date_received',axis=1,inplace=True)
    st.table(pred_df)
    #st.table(user_df)
    #st.table(result)
    #st.table(user_df)


