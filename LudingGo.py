# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 13:57:09 2020

@author: rahul

Note - This can be run from anaconda prompt using -  streamlit run "SteamLitFakeNews.py"

"""


import numpy as np
import streamlit as st
import pandas as pd
from PIL import Image
pd.set_option('precision',0)
image = Image.open('logo.png')
st.image(image,output_format='png')
st.markdown(
            f"""
            <style>
            .reportview-container .main .block-container{{
            max-width: {1500}px;
            padding-top: {0}rem;
            padding-right: {1}rem;
            padding-left: {1}rem;
            padding-bottom: {0}rem;
            }}
            .reportview-container .main {{
            color: {'Black'};
            background-color: {'White'};
            }}
            </style>
            """,
            unsafe_allow_html=True)

def Pricing_800():
    ##st.markdown("# 800 Pricing")
    ## select box (Unit & Date)
    st.markdown('### Select a Unit')
    ''
    units = []
    for i in range(2, 6):
        for j in range(1, 28):
            if len(str(j)) == 1:
                units.append(str(i) + '0' + str(j))
            else:
                units.append(str(i) + str(j))
    for i in range(1, 24):
        if len(str(i)) == 1:
            units.append('6' + '0' + str(i))
        else:
            units.append('6' + str(i))
    unit = st.selectbox('', units, index = 2)
    st.markdown('### Select a Move In Date')
    ''
    start_months = ['2021-04-01','2021-05-01','2021-06-01','2021-07-01','2021-08-01']
    start = st.selectbox('', start_months, index = 2)
    ''
    df = pd.DataFrame({"Rent": ['Base Price', 'Concession', 'Effective Rent'], 
                      "2021-12-31": [1, 2, 3],
                      "2022-01-31": [1, 2, 3],
                      "2022-02-31": [1, 2, 3],
                      "2022-03-31": [1, 2, 3],
                      "2022-04-31": [1, 2, 3],
                      "2022-05-31": [1, 2, 3],
                      "2022-06-31": [1, 2, 3],
                      "2022-07-31": [1, 2, 3]}).set_index(["Rent"])
    st.table(df)
    # end = st.selectbox('Lease To', months, index = 6)
    
    
    
#     df = pd.DataFrame(
#     np.random.randn(10, 20),
#     columns=('col %d' % i for i in range(20)))

#     st.dataframe(df.style.highlight_max(axis=0))
    
    
def run():
    st.sidebar.title('Navigation')
    page = st.sidebar.radio('',('800 Pricing',))
#     selector = st.sidebar.multiselect("Which would you like", [1, 2, 3], key="3")
#     st.write(selector)
    st.sidebar.title('About')
    st.sidebar.info('This app is develeoped by Data Team')
    Pricing_800()

if __name__ == "__main__":
    run()