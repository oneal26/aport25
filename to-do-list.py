tasks = []

# adds tasks 
def add_task(task_name):
    task.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' added! ")

# displays task with status
def view_tasks(tasks):
    if not tasks:
        print("Tasks not found.")
        return
    print("\n-- Your Tasks --")
    for i, task in enumerate(tasks):
        status = "Done" if task["Completed"] else " "
        print(f"{i + 1}. [{status}] {tasks['name']}")
    print("------------------")
    

# marks task complete
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        task[task_index] ["completed"] = True
        print(f"Task '{task[task_index]['name']}' marked as completed.")
    else:
        print("Invalid task number.")

# deletes task from list
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['name']}' deleted.")
    else:
        print("Invalid task number.")

# displays main menu options
def display_menu():
    print("\n--- Options Menu ---")
    print("1. Add Task")
    print("2. View Task")
    print("3. Delete Task")
    print("4. Complete Task")
    print("5. Exit")

# main function to run task manager 
def main():
    while True:
        display_menu()
        choice = input("Enter your choice." )

        if choice == '1':
            task_name = input("Enter the task name: ")
            add_task(task_name)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks() # Show tasks to help user pick
            try:
                task_num = int(input("Enter the number of the task to complete: ")) - 1
                complete_task(task_num)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            view_tasks() # Show tasks to help user pick
            try:
                task_num = int(input("Enter the number of the task to delete: ")) - 1
                delete_task(task_num)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '5':
            print("Exiting Task Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
        