import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'pyto_do'))

from storage_processor import load_tasks, save_tasks

# Load tasks from file

tasks = []

# Add a task

def add_task(task):
   tasks.append({"task": task, "completed": False})
   save_tasks(tasks)
   print(f"Added task: '{task}'")

# List tasks
def view_tasks():
   if not tasks:
      print("No tasks in your To-Do list")
   else:
      print("To-Do List:")
   for i, task in enumerate(tasks, 1): # start numbering from 1
        status = "✓" if task["completed"] else "✗"
        print(f"{i+1}. {task['task']} - {status}") 
        
# Mark task as completed
def complete_task(task_number):
    try:
        task = tasks[task_number-1]
    except IndexError:
        print("Invalid task number")
        return
    task["completed"] = True
    save_tasks(tasks)
    print(f"Completed task: '{task['task']}'")   
    
    # Remove task
    
def delete_task(task_number):
    try:
        task = tasks.pop(task_number-1)
    except IndexError:
        print("Invalid task number")
        return
    save_tasks(tasks)
    print(f"Deleted task: '{task['task']}'")
        
        # Main program loop
def menu():
 while True:
   print("\nChoose an option:")
   print("1. Add task")
   print("2. View tasks")
   print("3. Complete task")
   print("4. Delete task")
   print("5. Exit")
   choice = input("Choose an option: ")
   
   if choice == "1":
       task = input("Enter task: ")
       add_task(task)
   elif choice == "2":
       view_tasks()
   elif choice == "3":
       task_number = int(input("Enter task number: "))
       complete_task(task_number)
   elif choice == "4":
       task_number = int(input("Enter task number: "))
       delete_task(task_number)
   elif choice == "5":
       break
   else:
                print("Invalid choice")
                
if __name__ == "__main__":
   menu()