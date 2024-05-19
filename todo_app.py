import streamlit as st
import datetime

# Function to reset the to-do list every 24 hours
def reset_todo_list():
    current_date = datetime.datetime.now().date()
    if 'last_reset' not in st.session_state:
        st.session_state.last_reset = current_date
    if current_date != st.session_state.last_reset:
        st.session_state.todo_list = []
        st.session_state.last_reset = current_date

# Function to add a new task
def add_task():
    if 'todo_list' not in st.session_state:
        st.session_state.todo_list = []
    task = st.text_input('Enter a task', '')
    if st.button('Add Task'):
        if task:
            st.session_state.todo_list.append({'task': task, 'done': False})
            st.experimental_rerun()

# Function to update the status of a task
def update_task_status(index):
    st.session_state.todo_list[index]['done'] = not st.session_state.todo_list[index]['done']

# Function to display the to-do list
def display_todo_list():
    for i, item in enumerate(st.session_state.todo_list):
        task = item['task']
        done = item['done']
        if done:
            task = f"~~{task}~~"
        st.checkbox(task, value=done, key=f"task_{i}", on_change=update_task_status, args=(i,))

# Function to display the current date and day of the week
def display_date():
    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
    current_day = datetime.datetime.now().strftime("%A")
    st.markdown(f"<div style='text-align: right; font-weight: bold;'>Today is {current_date},{current_day}</div>", unsafe_allow_html=True)

# Main function
def main():
    st.title('Daily To-Do List')
    display_date()
    reset_todo_list()
    add_task()
    display_todo_list()

if __name__ == "__main__":
    main()
