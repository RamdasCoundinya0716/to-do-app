import streamlit as st
import json
import os
import datetime

# File to store tasks
TASKS_FILE = "tasks.json"

# Function to load tasks from a JSON file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

# Function to reset the to-do list at midnight
def reset_todo_list():
    current_date = datetime.datetime.now().date()
    if 'last_reset' not in st.session_state:
        st.session_state.last_reset = current_date
    if current_date != st.session_state.last_reset:
        st.session_state.todo_list = []
        st.session_state.last_reset = current_date
        save_tasks([])

# Function to add a new task
def add_task():
    task = st.text_input('Enter a task', '')
    if st.button('Add Task'):
        if task:
            st.session_state.todo_list.append({'task': task, 'done': False})
            save_tasks(st.session_state.todo_list)
            st.experimental_rerun()

# Function to update the status of a task
def update_task_status(index):
    st.session_state.todo_list[index]['done'] = not st.session_state.todo_list[index]['done']
    save_tasks(st.session_state.todo_list)

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
    st.markdown(f"<div style='text-align: right; font-weight: bold;'>{current_date} ({current_day})</div>", unsafe_allow_html=True)

# Main function
def main():
    st.title('Daily To-Do List')
    display_date()
    reset_todo_list()
    add_task()
    display_todo_list()

# Load tasks into session state
if 'todo_list' not in st.session_state:
    st.session_state.todo_list = load_tasks()
if 'last_reset' not in st.session_state:
    st.session_state.last_reset = datetime.datetime.now().date()

if __name__ == "__main__":
    main()
