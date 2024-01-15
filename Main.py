#Bismillah



import streamlit as st
import Functionsfortodo as functions

st.title("My Todo App")
st.subheader("Hi")

todos = functions.get_todos()

def add_todo():
    newtodo = st.session_state["todo_input"]
    todos.append(newtodo)
    functions.write_todos(todos)


for i in todos:
    st.checkbox(i)


st.text_input(label="nice",placeholder="Add new todo...",
              on_change=add_todo, key="todo_input")

print("Bismillah")

st.session_state