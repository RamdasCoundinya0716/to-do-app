# Streamlit Daily To-Do List App

This project is a daily to-do list app built with Python and Streamlit. The app allows users to add tasks, mark them as complete, and automatically resets the to-do list every 24 hours. It also displays the current date and day of the week at the top-right corner of the app. Tasks are persisted even if the page is refreshed.

## Features

- Add new tasks to the to-do list.
- Mark tasks as complete with a checkbox.
- Strikethrough tasks when marked as complete.
- Automatically reset the to-do list every 24 hours.
- Display the current date and day of the week at the top-right corner.
- Persist tasks even if the page is refreshed.

## Installation

### Using Python

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/streamlit-todo-list.git
    cd streamlit-todo-list
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the app:

    ```sh
    streamlit run todo_app.py
    ```

### Using Docker

1. Pull the Docker image:

    ```sh
    docker pull ram0716/to_do_app:v2
    ```

2. Run the Docker container:

    ```sh
    docker run -p 8501:8501 ram0716/to_do_app:v2
    ```

3. Open your web browser and go to `http://localhost:8501` to see the app.

## Usage

- Enter a task in the input field and click "Add Task" to add it to the list.
- Check the checkbox next to a task to mark it as complete. The task will be struck through.
- Uncheck the checkbox to undo the strike-through.
- The to-do list will automatically reset every 24 hours.
- The tasks will persist even if the page is refreshed.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.
