# Task Manager

## Project Overview

Task Manager is a Python-based application designed to help users organize and manage their daily tasks. The application allows users to add tasks, assign priorities, set task times, create reminders, mark tasks as completed, delete tasks, and view task statistics.

The project follows a modular Python structure where different functionalities are separated into individual modules.

## Problem Statement

Managing multiple daily tasks manually can make it difficult to keep track of task priorities, schedules, completion status, and reminders. This project provides a simple command-line Task Manager that organizes these details in one place.

## Objectives

* Add and manage daily tasks.
* Assign priorities to tasks.
* Assign a time of day to each task.
* Set reminders for pending tasks.
* Mark tasks as completed.
* Delete tasks.
* Display pending tasks and task summaries.
* Provide task statistics.
* Validate user inputs such as dates and reminder information.

## Features

* User name input and welcome message.
* Add multiple tasks.
* Store task dates.
* Assign High, Medium, or Low priority.
* Assign Morning, Afternoon, or Evening time.
* Set task reminders.
* Display pending tasks.
* Mark tasks as completed.
* Delete tasks.
* Display task summaries.
* Display task statistics.
* Input validation for dates and reminder information.

## Technologies Used

* Python 3
* Python Standard Library
* Command Line Interface (CLI)
* Git and GitHub for version control

## Project Structure

```text
Task-Manager/
│
├── main.py
├── README.md
├── statement.md
│
└── src/
    ├── __init__.py
    ├── task.py
    ├── task_manager.py
    ├── task_input.py
    ├── priority.py
    ├── reminder.py
    ├── display.py
    └── statistics.py
```

## Modules

### main.py

Controls the main workflow of the Task Manager application.

### task.py

Contains the `Task` class and task-related operations such as completing and deleting tasks.

### task_manager.py

Contains the `TaskManager` class for managing task data.

### task_input.py

Handles task name and date input and validates the date format.

### priority.py

Provides the priority-related module used by the main application.

### reminder.py

Handles reminder selection and reminder time input.

### display.py

Provides functionality for displaying task information.

### statistics.py

Provides the statistics module for task-related calculations.

## How to Run

### 1. Install Python

Install Python 3 on your computer.

### 2. Open the Project

Open a terminal inside the `Task-Manager` project folder.

### 3. Run the Application

```bash
python main.py
```

### 4. Follow the Instructions

The program will ask for:

* Your name
* Number of tasks
* Task details
* Task dates
* Priority
* Task time
* Reminder information
* Completed tasks
* Task deletion

## Testing

The application was tested for the following operations:

* Adding tasks
* Entering task dates
* Assigning task priorities
* Assigning task times
* Setting reminders
* Displaying pending tasks
* Completing tasks
* Deleting tasks
* Displaying task summaries
* Displaying task statistics
* Invalid date input
* Invalid reminder input

## Future Enhancements

Possible future improvements include:

* Graphical User Interface (GUI)
* Persistent database storage
* Editing existing tasks
* Recurring tasks
* Automatic scheduled notifications
* Search and filtering
* Improved input validation
* User authentication
* Exporting tasks to files

## Conclusion

The Task Manager provides a simple command-line solution for organizing daily tasks. Its modular structure separates different functionalities into individual Python modules, making the project easier to understand, maintain, test, and extend.

```

After saving it, **don't make any other files yet**.

Reply **`d`** when `README.md` is saved.
```
