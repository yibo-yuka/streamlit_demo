import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import requests
import json

#df = pd.read_excel("cost_of_global(in TWD_cleaned).xlsx")
#df = df.replace(" ", "")  # 將" "替換為空字串
#df = df.replace("NT$", "")  # 將"NT$"替換為空字串
#將除了CountryName以外的欄位轉換為數字
#cols = df.columns.tolist()
#for c in cols[1:-1]:
    #df[c] = [i[:-4] for i in df[c]]
    #df[c] = df[c].str.replace(",","")
    #df[c] = pd.to_numeric(df[c],errors = "coerce")
#print(df.info())
#df.to_csv("cost_of_global.csv", index=False)
#df = pd.read_csv("cost_of_global.csv")
#for col in df.columns[1:]:
    #df[col] = pd.to_numeric(df[col], errors='coerce')
#cols = df.columns.tolist()
#data_col = cols[:5]
#data_cols = cols[1:]  # 排除第一列CountryName
#val_df = df[data_col]
#country_list = df['CountryName'].tolist()

def load_data():
    url = "http://127.0.0.1:8000/api/numbeo/costs/"
    response = requests.get(url)
    if response.status_code == 200:
        posts_data = response.json()
        df = pd.DataFrame(posts_data)
        return df
    else:
        st.error("Failed to load data from the URL.")
        return None
df = load_data()
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col], errors='coerce')
cols = df.columns.tolist()
data_cols = cols[1:]  # 排除第一列CountryName
country_list = df['country_name'].tolist()
st.title("Numbeo Data Visualization")
#使用單選選單來選擇要顯示的資料
data_col = st.selectbox("Select data to display", data_cols)
#使用一個多選下拉選單來選擇國家
selected_countries = st.multiselect("Select countries", country_list)
#如果被選上的國家，則取出val_df中對應的資料
if selected_countries:
    filtered_df = df[df['country_name'].isin(selected_countries)]
    #使用plotly express來畫出長條圖
    fig = px.bar(filtered_df[cols], x='country_name', y=filtered_df[data_col],
                  title='Cost of Global in TWD',
                    labels={'value': 'Cost in TWD', 'variable': 'Country'})
    st.plotly_chart(fig, use_container_width=True)