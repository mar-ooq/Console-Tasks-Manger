def get_next_task_number(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
        task_numbers = []
        for line in lines:
            line = line.strip()
            if line.startswith("Task"):
                # Extract the task number after "Task"
                task_number = line.split(" ")[1].strip(":")
                if task_number.isdigit():
                    task_numbers.append(int(task_number))
        # Get the highest task number
        highest_task_number = max(task_numbers) if task_numbers else 0
        return highest_task_number + 1
    except FileNotFoundError:
        # If the file doesn't exist, start with Task 1
        return 1

def new_task(file_path):
    while True:
        task_number = get_next_task_number(file_path)
        task_name = input("Enter task name: ")
        task_category = input("Enter task category: ")
        task_priority = input("Enter task priority: ")
        task_status = input("Enter task status: ")
        task = (
            f"Task {task_number}:\n"
            f"Name: {task_name}\n"
            f"Category: {task_category}\n"
            f"Priority: {task_priority}\n"
            f"Status: {task_status}\n\n"
        )
        print("Do you want to add this task?")
        answer = input("Yes or No: ")
        match answer.lower():
            case "yes":
                with open(file_path, "a") as file:
                    file.write(task)
                print("Task added successfully!")
                break
            case "no":
                print("Let's try again.")
            case _:
                print("Invalid option. Please try again.")
                continue