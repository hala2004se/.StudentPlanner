# Shows the menu options to the user.
# The user can choose what to do.
# Output: Displays the menu.

def display_menu():
    print("\nSTUDENT PLANNER")
    print("----------------------------------------")
    print("1. Add a task")
    print("2. Edit a task")
    print("3. Delete a task")
    print("4. Find a task by ID")
    print("5. List all tasks")
    print("6. List tasks by course")
    print("7. List tasks by priority")
    print("8. Mark a task as completed")
    print("9. View task summary")
    print("10. Exit")
    print("----------------------------------------")


# Gets text from the user.
# Checks that the user did not leave the input empty.
# Output: Returns the entered text.

def get_text(prompt):
    text = input(prompt).strip()

    while text == "":
        print("Error: This field cannot be empty.")
        text = input(prompt).strip()

    return text

# Checks if the date is written in the correct format.
# Checks the numbers and slash positions.
# Output: Returns True or False.

def is_valid_date(date):
    if len(date) != 10:
        return False

    for i in range(10):
        if i == 2 or i == 5:
            if date[i] != "/":
                return False
        else:
            if date[i] not in "0123456789":
                return False

    return True


# Asks the user to enter a due date.
# Keeps asking until the date format is correct.
# Output: Returns the date.

def get_date():
    date = input("Due date (DD/MM/YYYY): ").strip()

    while not is_valid_date(date):
        print("Error: Invalid date format. Use DD/MM/YYYY.")
        date = input("Due date (DD/MM/YYYY): ").strip()

    return date

# Asks the user to choose a task priority.
# The choices are High, Medium, and Low.
# Output: Returns the selected priority.

def get_priority():
    choice = input("Priority (1=High, 2=Medium, 3=Low): ").strip()

    while choice != "1" and choice != "2" and choice != "3":
        print("Error: Invalid priority.")
        choice = input("Priority (1=High, 2=Medium, 3=Low): ").strip()

    if choice == "1":
        return "High"
    elif choice == "2":
        return "Medium"
    else:
        return "Low"

# Asks the user to enter a task ID.
# Checks that the ID contains numbers only and is greater than zero.
# Output: Returns the ID or None if it is not valid.

def get_task_id():
    text = input("Enter task ID: ").strip()

    if text == "":
        print("Error: Task ID cannot be empty.")
        return None

    for ch in text:
        if ch not in "0123456789":
            print("Error: Task ID must contain digits only.")
            return None

    task_id = int(text)

    if task_id <= 0:
        print("Error: Task ID must be greater than zero.")
        return None

    return task_id

# Gets the task information from the user.
# Saves the information in a dictionary and adds it to the list.
# Output: Shows a success message and returns the next ID.

def add_task(tasks, next_task_id):
    title = get_text("Task title: ")
    course = get_text("Course name: ")
    due_date = get_date()
    priority = get_priority()

    task = {
        "id": next_task_id,
        "title": title,
        "course": course,
        "due_date": due_date,
        "priority": priority,
        "status": "Pending"
    }

    tasks.append(task)

    print("Task added successfully. Task ID:", next_task_id)

    return next_task_id + 1

# Searches for a task using its ID.
# Checks all tasks until the correct ID is found.
# Output: Returns the task or None if it is not found.

def find_task_by_id(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None

# Shows the information of a task.
# Prints the title, course, date, priority, and status.
# Output: Displays the task details.

def display_task(task):
    print("ID:", task["id"])
    print("Title:", task["title"])
    print("Course:", task["course"])
    print("Due date:", task["due_date"])
    print("Priority:", task["priority"])
    print("Status:", task["status"])

# Allows the user to change task information.
# The user can choose which part to edit.
# Output: Shows if the task was updated or not.

def edit_task(tasks):
    task_id = get_task_id()

    if task_id is None:
        return

    task = find_task_by_id(tasks, task_id)

    if task is None:
        print("Task not found.")
        return

    print("1. Title")
    print("2. Course")
    print("3. Due date")
    print("4. Priority")
    print("5. Cancel")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        task["title"] = get_text("Task title: ")

    elif choice == "2":
        task["course"] = get_text("Course name: ")

    elif choice == "3":
        task["due_date"] = get_date()

    elif choice == "4":
        task["priority"] = get_priority()

    elif choice == "5":
        print("Edit cancelled.")
        return

    else:
        print("Error: Invalid choice.")
        return

    print("Task updated successfully.")

# Removes a task from the list.
# Searches for the task using its ID before deleting it.
# Output: Shows if the task was deleted or not.

def delete_task(tasks):
    task_id = get_task_id()

    if task_id is None:
        return

    task = find_task_by_id(tasks, task_id)

    if task is None:
        print("Task not found.")
    else:
        tasks.remove(task)
        print("Task deleted successfully.")
