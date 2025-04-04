from read_tasks import read_tasks

def delete_task(file_path):
    # Fetch tasks from the file
    tasks_list = read_tasks(file_path)

    # Display tasks to the user
    if not tasks_list:
        print("No tasks found.")
        return

    print("Your tasks:")
    print("--------------------------------")
    for index, task in enumerate(tasks_list, start=1):
        print(f"Task {index}:")
        for key, value in task.items():
            print(f"{key}: {value}")
        print("--------------------------------")

    # Prompt the user to delete a task
    try:
        task_to_delete = int(input("Enter the number of the task you want to delete: "))
        if 1 <= task_to_delete <= len(tasks_list):
            tasks_list.pop(task_to_delete - 1)  # Remove the selected task
        else:
            print("Invalid task number.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
        return

    # Save the updated tasks back to the file with updated Task numbers
    with open(file_path, "w") as file:
        for index, task in enumerate(tasks_list, start=1):
            file.write(
                f"Task {index}:\n"
                f"Name: {task['Name']}\n"
                f"Category: {task['Category']}\n"
                f"Priority: {task['Priority']}\n"
                f"Status: {task['Status']}\n\n"
            )
    print("Task deleted successfully!")