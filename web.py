import streamlit as st
import function

todos = function.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    function.write_todos(todos)

st.title("My Todo App")
st.subheader("this is my todo app")
st.write("this app will inc your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a Todo", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')