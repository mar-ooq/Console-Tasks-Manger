from new_task import new_task
from delete_task import delete_task
from change_task_status import change_task_status
from read_tasks import read_tasks
from change_task_data import change_task_data

file_path = "./tasks.txt"
# Welcome page
print("Hello!")
print("What we doing today?")
print("1. Add new task")
print("2. Delete task")
print("3. Change task status")
print("4. Change task data")
print("5. Show tasks list")

while True:
    choice = input()
    match choice:
        case "1" | "1." | "Add new task" | "add new task":
            new_task(file_path) #done
            break
        case "2" | "2." | "delete task" | "delete task":
            delete_task(file_path)  #done
            break
        case "3" | "3." | "Change task status" | "change task status":
            change_task_status(file_path) #done
            break
        case "4" | "4." | "Change task data" | "change task data":
            change_task_data(file_path) #done
            break
        case "5" | "5." | "Show tasks list" | "show tasks list":
            tasks = read_tasks(file_path)
            print("--------------------------------")
            for task in tasks:
                for key, value in task.items():
                    print(f"{key}: {value}")
                print("--------------------------------")
            break
        case _:
            print("Invalid option. Please try again.")

