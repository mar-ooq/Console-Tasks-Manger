def read_tasks(file_path):
    tasks = []
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            task = {}
            for line in lines:
                line = line.strip()
                if line.startswith("Task"):
                    if task:  # Append the previous task before starting a new one
                        tasks.append(task)
                    task = {}  # Start a new task
                elif line.startswith("Name:"):
                    task["Name"] = line.split(":")[1].strip()
                elif line.startswith("Category:"):
                    task["Category"] = line.split(":")[1].strip()
                elif line.startswith("Priority:"):
                    task["Priority"] = line.split(":")[1].strip()
                elif line.startswith("Status:"):
                    task["Status"] = line.split(":")[1].strip()
            if task:  # Append the last task after finishing the loop
                tasks.append(task)
        return tasks
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

# if __name__ == "__main__":
#     # Test code only runs when this file is executed directly
#     tasks = read_tasks("tasks.txt")
#     print(tasks)


