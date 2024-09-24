import streamlit as st

columns = st.columns([1, 2, 1])

with columns[1]:
  st.title("Greek Life Quiz")
  st.image("crest.png")

with st.expander("About"):
      st.write("This application is designed to help my fellow pledges learn about different fraternities and sororities on campus for associate member education through a fun and interactive quiz.")
      st.write("Developed by Daniel Crow.")

st.sidebar.success("Select a page above.")