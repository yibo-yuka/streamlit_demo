import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")
st.button("Click Me!")
st.text_input("Enter some text:")
st.slider("Select a value:", 0, 100, 50)
st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.multiselect("Select multiple options:", ["Option A", "Option B", "Option C"])