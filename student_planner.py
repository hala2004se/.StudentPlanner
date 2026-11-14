#Group members:
#1.Name: Hala Maher Bouzalasal | Student ID: 447205183 | Section:78701
#2.Name: Layla Alshilash | Student ID: 447202579 | Section : 78701

#Shows the menu options to the user.
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

def list_all_tasks(tasks):
    if tasks == []:
        print("There are no tasks.")
    else:
        for task in tasks:
            display_task(task)
# Displays all tasks in the list. If there are no tasks, displays a message: "There are no tasks."

def list_tasks_by_course(tasks):
        course_name= input("Enter course name or code:")
        while course_name.strip() == "":
            print("Invalid input")
            course_name= input("Enter course name or code:")
        found = False
        for task in tasks:
            if course_name.lower() == task["course"].lower():
                found = True
                display_task(task)
        if found == False:
            print("No tasks found for this course.")
# Asks the user to enter either a course name or code, then searches for and displays all tasks related to it.

def list_tasks_by_priority(tasks):
    priority_level = input("Enter priority (keep in mind that: 1= High, 2=Medium, 3=Low): ").strip()
    while True:
        if priority_level == "":
            print("Invalid choice")
            priority_level = input("Enter priority (keep in mind that: 1= High, 2=Medium, 3=Low): ").strip()
        elif priority_level.isdigit():
            if 3 < int(priority_level) or int(priority_level) < 1:
                print("Invalid choice")
                priority_level = input("Enter priority (keep in mind that: 1= High, 2=Medium, 3=Low): ").strip()
            else:
                break
        else:
            print("Invalid choice")
            priority_level = input("Enter priority (keep in mind that: 1= High, 2=Medium, 3=Low): ").strip()
    found = False
    if int(priority_level) == 1:
        priority_level = "High"
        print("--- High Priority Tasks ---")
        for task in tasks:
            if priority_level == task["priority"]:
                found = True
                display_task(task)
    elif int(priority_level) == 2:
        priority_level = "Medium"
        print("--- Medium Priority Tasks ---")
        for task in tasks:
            if priority_level == task["priority"]:
                found = True
                display_task(task)
    elif int(priority_level) == 3:
        priority_level = "Low"
        print("--- Low Priority Tasks ---")
        for task in tasks:
            if priority_level == task["priority"]:
                found = True
                display_task(task)
    if not found:
        print(f"No tasks found with {priority_level} priority")
# Asks the user to enter a priority level (High, Medium, or Low), then displays all tasks that match the selected priority.

def mark_task_completed(tasks):
    number_task_ID = input("Enter number ID task to change it into 'completed': ").strip()
    while True:
        if number_task_ID.isdigit():
            number_task_ID = int(number_task_ID)
            if number_task_ID <= 0:
                print("Invalid")
                number_task_ID = input("Enter task ID to change it into 'completed' :").strip()
            else:
                break
        else:
            print("Invalid")
            number_task_ID = input("Enter task ID to change it into 'completed' :").strip()
    taskID_ToSearch = find_task_by_id(tasks, number_task_ID)
    if taskID_ToSearch is not None:
        if taskID_ToSearch["status"] == "Completed":
            print(f"Task {number_task_ID} is already Completed")
        else:
            taskID_ToSearch["status"] = "Completed"
            print(f"Task {number_task_ID} marked as Completed")
    else:
        print(f"Task {number_task_ID} is not found")
# Allows the user to change a task's status from Pending to Completed, after making sure that the task exists in the list and has not already been completed.

def show_summary(tasks):
    Total_tasks = len(tasks)
    count_for_Pending = 0
    count_for_completed = 0
    if tasks != []:
        for task in tasks:
            if task["status"] == "Pending":
                count_for_Pending += 1
            elif task["status"] == "Completed":
                count_for_completed += 1
        completion_Percentage = (count_for_completed / Total_tasks) * 100
        print(f"Total tasks: {Total_tasks}")
        print(f"Completed tasks: {count_for_completed}")
        print(f"Pending tasks: {count_for_Pending}")
        print(f"Completion Percentage: {completion_Percentage:.1f}%")
    if tasks == []:
        print("Total tasks: 0")
        print("Completed tasks: 0")
        print("Pending tasks: 0")
        print("Completion Percentage: 100.0%")
# Displays a summary of the tasks, including the total number of tasks, the number of completed tasks, the number of pending tasks, and the completion percentage.

def main():
    tasks = []
    next_task_id = 1
    while True:
        display_menu()
        user_choice = input("Enter number from the menu:").strip()
        while True:
            if user_choice == "":
                print("Invalid choice")
                user_choice = input("Enter number from the menu:").strip()
            elif user_choice.isdigit():
                if int(user_choice) <= 0 or int(user_choice) > 10:
                    print("Invalid choice")
                    user_choice = input("Enter number from the menu:").strip()
                else:
                    break
            else:
                print("Invalid choice")
                user_choice = input("Enter number from the menu:").strip()
        if int(user_choice) == 1:
            next_task_id = add_task(tasks, next_task_id)
        elif int(user_choice) == 2:
            edit_task(tasks)
        elif int(user_choice) == 3:
            delete_task(tasks)
        elif int(user_choice) == 4:
            task_id= input("Enter task ID: ").strip()
            while True:
                if task_id == "":
                    print("Invalid task ID")
                    task_id = input("Enter task ID: ").strip()
                elif task_id.isdigit():
                    if int(task_id) <= 0:
                        print("Invalid")
                        task_id = input("Enter task ID: ").strip()
                    else:
                        break
                else:
                    print("Invalid task ID")
                    task_id = input("Enter task ID: ").strip()
            task_id = int(task_id)
            task= find_task_by_id(tasks, task_id)
            if task == None:
                print("Task not found")
            else:
                display_task(task)
        elif int(user_choice) == 5:
            list_all_tasks(tasks)
        elif int(user_choice) == 6:
            list_tasks_by_course(tasks)
        elif int(user_choice) == 7:
            list_tasks_by_priority(tasks)
        elif int(user_choice) == 8:
            mark_task_completed(tasks)
        elif int(user_choice) == 9:
            show_summary(tasks)
        elif int(user_choice) == 10:
            print("Goodbye! Thank you for using Student Planner.")
            break
        else:
            print("Invalid choice")
# The main function controls the program. It creates the tasks list, displays the menu, receives the user's choice, and calls the appropriate function. The function continues running until the user chooses option 10.

main()

