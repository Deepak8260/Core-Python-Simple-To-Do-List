To-Do List Application
======================

A simple, interactive Python-based To-Do List application that allows users to manage their tasks. Users can add, view, edit, and delete tasks, providing a practical way to practice fundamental Python concepts like control flow, data structures, and user input handling.

Features:
---------

*   **Add a Task**: Users can enter new tasks to be added to the list.
    
*   **View Tasks**: Users can see a list of all the tasks they’ve added.
    
*   **Edit Tasks**: Users can modify the details of an existing task.
    
*   **Delete Tasks**: Users can remove tasks they no longer need.
    
*   **Interactive Menu**: The program presents a menu to guide users through their task management.
    

Technologies:
-------------

*   Python 3.x
    
*   Basic Python libraries (No external dependencies)
    

Requirements:
-------------

*   Python 3.x or higher
    
*   A text editor or IDE for Python development (e.g., Visual Studio Code, PyCharm)
    

Installation:
-------------

1.  bashCopy codegit clone
    
2.  bashCopy codecd todo-list
    
3.  bashCopy codepython todo.py
    

How to Use:
-----------

Once you run the program, you’ll be presented with a simple menu with the following options:

1.  **Add a Task**: Select this option to add a new task. You will be prompted to enter the task description.
    
2.  **View Tasks**: This option displays a list of all tasks currently in the To-Do List.
    
3.  **Edit a Task**: Select this option if you want to modify an existing task. You’ll need to specify the task number and provide the updated details.
    
4.  **Delete a Task**: This option allows you to delete a task. You’ll need to specify the task number to remove it.
    
5.  **Exit**: Exit the application when you’re done.
    

The program will loop back to the main menu after each action, allowing you to continue managing tasks until you choose to exit.

Code Explanation:
-----------------

*   **Functions**: The core functionality of the program is divided into separate functions to handle tasks like adding, viewing, editing, and deleting tasks.
    
    *   add\_task(): Allows the user to input a new task and adds it to the list.
        
    *   view\_tasks(): Displays all the tasks currently in the list.
        
    *   edit\_task(): Lets the user modify an existing task by selecting the task number.
        
    *   delete\_task(): Prompts the user to select a task to delete by its number.
        
*   **Control Flow**: The application uses a while loop to continuously show the menu until the user chooses to exit. Conditional statements are used to determine which action to take based on user input.
    
*   **Data Structures**:
    
    *   The tasks are stored in a **list**, where each task is represented as a string.
        
    *   The task list is updated dynamically as tasks are added, edited, or removed.
        
*   **Input Validation**: Basic validation checks are in place for user input to ensure that valid task numbers are entered for editing or deleting.
    

Example Run:
------------

```bash
Welcome to the To-Do List Application!
Please select an option:
1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Exit

Enter your choice: 1
Enter your task: Buy groceries
Task added!

----------------------------------------

Please select an option:
1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Exit

Enter your choice: 2
Tasks:
1. Buy groceries

----------------------------------------

Please select an option:
1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Exit

Enter your choice: 3
Enter the task number to edit: 1
Enter the new task: Buy groceries and fruits
Task edited!

----------------------------------------

Please select an option:
1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Exit

Enter your choice: 2
Tasks:
1. Buy groceries and fruits

----------------------------------------

Please select an option:
1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Exit

Enter your choice: 4
Enter the task number to delete: 1
Task deleted!

----------------------------------------

Please select an option:
1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Exit

Enter your choice: 2
No tasks available.

----------------------------------------

Please select an option:
1. Add Task
2. View Tasks
3. Edit Task
4. Delete Task
5. Exit

Enter your choice: 5
Goodbye!


```


Contributing:
-------------

If you would like to contribute to the development of this project, feel free to fork the repository, make your changes, and create a pull request with your improvements or fixes. We welcome contributions to improve the functionality or UI of the To-Do List application.

License:
--------

This project is open-source and licensed under the MIT License.
