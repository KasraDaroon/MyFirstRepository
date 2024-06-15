def add_task(task_list, task):
    
    task_list.append(task)
    
    print("Task added successfully!")

def remove_task(task_list, task):
    
    if task in task_list:
       
        task_list.remove(task)
   
        print("Task removed successfully!")
   
    else:
   
        print("Task not found in the list.")

def view_tasks(task_list):

    if task_list:

        print("Current Task List:")

        for idx, task in enumerate(task_list, 1):

            print(f"{idx}. {task}")

    else:

        print("Task list is empty.")


def save_tasks(task_list, filename):

    try:

        with open(filename, 'w') as file:

            for task in task_list:

                file.write(task + '\n')

        print("Tasks saved to file successfully!")

    except IOError:

        print("Error saving tasks to file.")

def load_tasks(filename):

    try:

        with open(filename, 'r') as file:

            task_list = [line.strip() for line in file.readlines()]

        print("Tasks loaded from file successfully!")

        return task_list

    except IOError:

        print("Error loading tasks from file.")

        return []

def handle_exceptions(func, *args):

    try:

        func(*args)

    except Exception as e:

        print(f"Error: {e}")