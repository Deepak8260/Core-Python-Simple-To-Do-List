# A simple To-Do List Application

# List to store tasks
tasks = []

# Function to display all tasks
def display_tasks():
    if not tasks:
        print("\nNo tasks in your to-do list.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
            
# Function to add a task
def add_task():
    task = input("\nEnter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added to your to-do list.")
    
# Function to edit an existing task
def edit_task():
    display_tasks()
    try:
        task_number = int(input("\nEnter the task number you want to edit: "))
        if 1 <= task_number <= len(tasks):
            new_task = input("Enter the new task description: ")
            tasks[task_number - 1] = new_task
            print(f"Task #{task_number} updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete a task
def delete_task():
    display_tasks()
    try:
        task_number = int(input("\nEnter the task number you want to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main menu function to display options and take user input
def main_menu():
    while True:
        print("\nTo-Do List Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            display_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Running the program
if __name__ == "__main__":
    main_menu()
