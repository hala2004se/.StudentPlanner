
# Shows the menu options to the user.
# The user can choose what to do.
# Output: Displays the menu on the screen.
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


# Gets the task information from the user.
# Checks the inputs and saves the task in a dictionary.
# Output: Shows a success message and returns the next task ID.
def add_task(tasks, next_task_id):
    title = input("Task title: ").strip()
    while title == "":
        print("Error: Title cannot be empty.")
        title = input("Task title: ").strip()

    course = input("Course name: ").strip()
    while course == "":
        print("Error: Course name cannot be empty.")
        course = input("Course name: ").strip()

    while True:
        due_date = input("Due date (DD/MM/YYYY): ").strip()
        valid = len(due_date) == 10
        if valid:
            for i in range(10):
                if i == 2 or i == 5:
                    if due_date[i] != "/":
                        valid = False
                elif due_date[i] not in "0123456789":
                    valid = False
        if valid:
            break
        print("Error: Invalid date format. Use DD/MM/YYYY.")

    while True:
        choice = input("Priority (1=High, 2=Medium, 3=Low): ").strip()
        if choice == "1":
            priority = "High"
            break
        elif choice == "2":
            priority = "Medium"
            break
        elif choice == "3":
            priority = "Low"
            break
        print("Error: Invalid priority. Enter 1, 2, or 3.")

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
# Prints the ID, title, course, date, priority, and status.
# Output: Displays the task details on the screen.
def display_task(task):
    print("ID:", task["id"])
    print("Title:", task["title"])
    print("Course:", task["course"])
    print("Due date:", task["due_date"])
    print("Priority:", task["priority"])
    print("Status:", task["status"])


# Allows the user to change task information.
# The user can choose which part of the task to edit.
# Output: Shows a success message or an error message.
def edit_task(tasks):
    text = input("Enter task ID: ").strip()
    if text == "":
        print("Error: Task ID cannot be empty.")
        return
    for ch in text:
        if ch not in "0123456789":
            print("Error: Task ID must contain digits only.")
            return
    task_id = int(text)
    if task_id == 0:
        print("Error: Task ID must be greater than zero.")
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
    field = input("Enter your choice: ").strip()

    if field == "1":
        new_title = input("Task title: ").strip()
        while new_title == "":
            print("Error: Title cannot be empty.")
            new_title = input("Task title: ").strip()
        task["title"] = new_title

    elif field == "2":
        new_course = input("Course name: ").strip()
        while new_course == "":
            print("Error: Course name cannot be empty.")
            new_course = input("Course name: ").strip()
        task["course"] = new_course

    elif field == "3":
        while True:
            new_date = input("Due date (DD/MM/YYYY): ").strip()
            valid = len(new_date) == 10
            if valid:
                for i in range(10):
                    if i == 2 or i == 5:
                        if new_date[i] != "/":
                            valid = False
                    elif new_date[i] not in "0123456789":
                        valid = False
            if valid:
                break
            print("Error: Invalid date format. Use DD/MM/YYYY.")
        task["due_date"] = new_date

    elif field == "4":
        while True:
            choice = input("Priority (1=High, 2=Medium, 3=Low): ").strip()
            if choice == "1":
                task["priority"] = "High"
                break
            elif choice == "2":
                task["priority"] = "Medium"
                break
            elif choice == "3":
                task["priority"] = "Low"
                break
            print("Error: Invalid priority. Enter 1, 2, or 3.")

    elif field == "5":
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
    text = input("Enter task ID: ").strip()
    if text == "":
        print("Error: Task ID cannot be empty.")
        return
    for ch in text:
        if ch not in "0123456789":
            print("Error: Task ID must contain digits only.")
            return
    task_id = int(text)
    if task_id == 0:
        print("Error: Task ID must be greater than zero.")
        return

    task = find_task_by_id(tasks, task_id)
    if task is None:
        print("Task not found.")
    else:
        tasks.remove(task)
        print("Task deleted successfully.")


