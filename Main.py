#Bismillah



import streamlit as st
import Functionsfortodo as functions

st.title("My Todo App")
st.subheader("Hi")

todos = functions.get_todos()

def add_todo():
    newtodo = st.session_state["todo_input"] + "\n"
    todos.append(newtodo)
    functions.write_todos(todos)



for i, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()



st.text_input(label="",placeholder="Add new todo...",
              on_change=add_todo, key="todo_input")