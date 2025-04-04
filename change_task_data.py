from read_tasks import read_tasks

def change_task_data(file_path):
    tasks_list = read_tasks(file_path)
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

    try:
        task_to_change_data_of = int(input("Enter the number of the task you want to change status: "))
        if 1 <= task_to_change_data_of <= len(tasks_list):
            new_name = input("Enter the new name: ")
            new_category = input("Enter the new category: ")
            new_priority = input("Enter the new priority: ")
            new_status = input("Enter the new status: ")
            tasks_list[task_to_change_data_of - 1].update({"Name": new_name, "Category": new_category, "Priority": new_priority, "Status": new_status})
            # Save the updated tasks back to the file
            with open(file_path, "w") as file:
                for index, task in enumerate(tasks_list, start=1):
                    file.write(
                        f"Task {index}:\n"
                        f"Name: {task['Name']}\n"
                        f"Category: {task['Category']}\n"
                        f"Priority: {task['Priority']}\n"
                        f"Status: {task['Status']}\n\n"
                    )
            print("Task status updated successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")
        return

