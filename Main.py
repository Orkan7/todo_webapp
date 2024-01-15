#Bismillah



import streamlit as st
import Functionsfortodo as functions

st.title("My Todo App")
st.subheader("Hi")


todos = functions.get_todos()

for i in todos:
    st.checkbox(i)


st.text_input(label="nice",placeholder="Add new todo:")

print("Bismillah")