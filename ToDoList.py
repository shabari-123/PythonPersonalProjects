#TodoList App
def show_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        i=1
        for task in tasks:
            print(f"{i}. {task}")
            i+=1


def todo_app():
    tasks = []

    while True:
        print("\n=== To-Do List Menu ===")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # Add Task
        if choice == '1':
            task = input("Enter new task: ")
            tasks.append(task)
            print("Task added successfully!")

        # Show Tasks
        elif choice == '2':
            show_tasks(tasks)

        # Edit Task
        elif choice == '3':
            show_tasks(tasks)
            try:
                task_num = int(input("Enter task number to edit: "))
                if 1 <= task_num <= len(tasks):
                    new_task = input("Enter updated task: ")
                    tasks[task_num - 1] = new_task
                    print("Task updated successfully!")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        # Delete Task
        elif choice == '4':
            show_tasks(tasks)
            try:
                task_num = int(input("Enter task number to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Deleted task: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

        # Exit
        elif choice == '5':
            print("Exiting To-Do List App. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run the app
todo_app()