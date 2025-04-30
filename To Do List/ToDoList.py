import os
from datetime import datetime

TASKS_FILE = "tasks.txt"

# Load tasks from text file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if '|' in line:
                    parts = line.strip().split('|')
                    if len(parts) == 3:
                        title, status, due_date = parts
                        tasks.append({
                            "title": title,
                            "completed": status == "Completed",
                            "due_date": due_date.strip()
                        })
                    else:
                        title, status = parts
                        tasks.append({
                            "title": title,
                            "completed": status == "Completed",
                            "due_date": "No due date"
                        })
    return tasks

# Save tasks to text file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            status = "Completed" if task['completed'] else "Pending"
            due_date = task.get('due_date', "No due date")
            file.write(f"{task['title']}|{status}|{due_date}\n")

# Display tasks with warnings
def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
    else:
        today = datetime.today().date()
        print("\n--- Your To-Do List ---")
        for idx, task in enumerate(tasks, 1):
            status = "✅ Completed" if task['completed'] else "❌ Pending"
            due_date = task.get('due_date', "No due date").strip()
            warning = ""

            if due_date.lower() != "no due date":
                try:
                    due = datetime.strptime(due_date, "%Y-%m-%d").date()
                    if due < today and not task['completed']:
                        warning = "⚠️ Overdue!"
                    elif due == today and not task['completed']:
                        warning = "🕒 Due Today!"
                except ValueError:
                    warning = "❓ Invalid Date Format"

            print(f"{idx}. {task['title']} [{status}] (Due: {due_date}) {warning}")
        print()

# Add multiple tasks with validated date
def add_tasks(tasks):
    task_input = input("Enter tasks separated by commas: ").strip()
    task_list = [task.strip() for task in task_input.split(",") if task.strip()]
    
    if task_list:
        for task in task_list:
            while True:
                due_date = input(f"Enter due date for '{task}' (format: YYYY-MM-DD or leave blank): ").strip()
                if not due_date:
                    due_date = "No due date"
                    break
                try:
                    datetime.strptime(due_date, "%Y-%m-%d")
                    break
                except ValueError:
                    print("⚠️ Invalid date format. Please use YYYY-MM-DD.")
            tasks.append({"title": task, "completed": False, "due_date": due_date})
        print(f"Added {len(task_list)} task(s) successfully.")
    else:
        print("No valid tasks entered.")

# Mark a task as complete
def mark_task_complete(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            print(f"Task '{tasks[task_num - 1]['title']}' marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    show_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed['title']}' deleted successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop
def main():
    tasks = load_tasks()

    while True:
        print("\n====== To-Do List Menu ======")
        print("1. View Tasks")
        print("2. Add Multiple Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_tasks(tasks)
        elif choice == '2':
            add_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please select between 1 and 5.")

if __name__ == "__main__":
    main()
