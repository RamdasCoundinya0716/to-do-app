# Streamlit Daily To-Do List App

This project is a daily to-do list app built with Python and Streamlit. The app allows users to add tasks, mark them as complete, and automatically resets the to-do list every 24 hours. It also displays the current date and day of the week at the top-right corner of the app.

## Features

- Add new tasks to the to-do list.
- Mark tasks as complete with a checkbox.
- Strikethrough tasks when marked as complete.
- Automatically reset the to-do list every 24 hours.
- Display the current date and day of the week at the top-right corner.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/RamdasCoundinya0716/to-do-app.git
    cd streamlit-todo-list
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install streamlit
    ```

## Usage

1. Run the Streamlit app:

    ```sh
    streamlit run todo_app.py
    ```

2. Open your web browser and go to `http://localhost:8501` to view the app.

3. Use the text input to add new tasks to the list. Click the "Add Task" button to add the task.

4. Check the box next to a task to mark it as complete. The task will be struck through. Uncheck the box to undo this action.

5. The to-do list resets every 24 hours, clearing all tasks.

## Code Overview

- `todo_app.py`: The main Python script containing the Streamlit app.

### Key Functions

- `reset_todo_list()`: Resets the to-do list every 24 hours.
- `add_task()`: Adds a new task to the to-do list.
- `update_task_status(index)`: Toggles the 'done' status of a task.
- `display_todo_list()`: Displays the tasks with checkboxes.
- `display_date()`: Displays the current date and day of the week at the top-right corner.

### Using Docker

1. Build the Docker image:

    ```sh
    docker build -t streamlit-todo-list .
    ```

2. Run the Docker container:

    ```sh
    docker run -p 8501:8501 streamlit-todo-list
    ```

3. Open your web browser and go to `http://localhost:8501` to see the app.

## Usage

- Enter a task in the input field and click "Add Task" to add it to the list.
- Check the checkbox next to a task to mark it as complete. The task will be struck through.
- Uncheck the checkbox to undo the strike-through.
- The to-do list will automatically reset every 24 hours.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
