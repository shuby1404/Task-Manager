from datetime import datetime


from src.task import Task
from src.task_manager import TaskManager
from src.priority import choose_priority
from src.task_input import get_task_details
from src.reminder import set_reminder
from src.display import show_tasks
from src.statistics import show_statistics


#  TASK MANAGER 

name = input("Enter your name: ")

print()
print("Welcome", name)
print()

tasks = []
status = []
priority = []
task_date = []
time = []
reminder = []
reminder_time = []

print("ADD YOUR TASKS FOR TODAY")
print()

number = int(input("How many tasks do you want to add? "))

tasks = [""] * number
status = ["Pending"] * number
priority = [""] * number
task_date = [""]* number
time = [""]* number
reminder = [""] * number
reminder_time = [""] * number

print()
print(number, "tasks will be added.")

# Adding tasks

for i in range(number):
    task_name, date_value = get_task_details(i)
    tasks[i] = task_name
    task_date[i] = date_value

    print()
    print("Choose priority")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    priority = choose_priority(priority, i)
    choice = int(input("Enter priority: "))
    if choice == 1:

        if 1 in priority:
            print("high priority is already used")
            priority[i] = 0
        else:
            priority[i] = 1
        

    elif choice == 2:

        if 2 in priority:
            print("medium priority is already used")

            if 1 not in priority:
                priority[i] = 1
                print("hingh priority selected")

        else:    
            priority[i] = 2
        

    elif choice == 3:

        if 3 in priority:
            print("low priority is already used")

            if 1 not in priority:
                priority[i] = 1
                print("high priority selected")

            elif 2 not in priority:
                priority[i] = 2
                print("medium priority selected")    

        else:    
            priority[i] = 3
        

    else:
        print("invalid priority number")
        

        if 1 not in priority:
            priority[i] = 1

        elif 2 not in priority:
            priority[i] = 2

        elif 3 not in priority:
            priority[i] = 3         

    print("Task added successfully")
    print()

# Showing tasks

print("YOUR TASKS")

for i in range(number):

    print(i + 1, ".", tasks[i])
    print("Date:", task_date[i])
    print("Priority:", priority[i])
    print("Status:", status[i])
    print()

#task time

time = [""]* number

print()
print(" TASK TIME")

for i in range(number):
    print("Task:", tasks[i])
    print("1. Morning")
    print("2. Afternoon")
    print("3. Evening")

    choice = int(input("when do you want to do this task? "))

    if choice == 1:
        time[i] = "Morning"

    elif choice == 2:
        time[i] = "Afternoon"

    elif choice == 3:
        time[i] = "Evening"

    else: 
        time[i] = "Not decided"

    print()    

# TASK REMINDER

print()
print(" TASK REMINDER ")

for i in range(number):
    print("Task:", tasks[i])
    print("1. Yes")
    print("2. No")
    
    reminder, reminder_time = set_reminder(
        reminder, reminder_time, i, tasks)


    print()    


# Completing tasks

print("COMPLETE TASK ")
print("enetr 0 when you are finished")

while True:
    task_number = int(input("Which task did you complete? "))
    if task_number == 0:
        break

    elif task_number >= 1 and task_number <= number:

        status[task_number - 1] =  "Completed"

        print("Task", task_number, "marked as completed!")

else:

    print("Invalid task number.")


# Updated tasks

print()
print(" UPDATED TASKS ")

for i in range(number):

    print(i + 1, ".", tasks[i])
    print("Date:", task_date[i])
    print("Priority:", priority[i])
    print("Time:", time[i])
    print("Reminder:", reminder[i])
    print("Reminder Time:", reminder_time[i])
    if status[i] == "Pending" and reminder[i] == "Yes":

        print("Reminder Status:",
            "You have a task pending for", reminder_time[i])
    print("Status:", status[i])
    print()

# Showing pending teasks

print()
print(" PENDING TASKS")

for i in range(number):

    if status[i] == "Pending":
        print(i + 1, ".", tasks[i])
        print("Date:", task_date[i])
        print("Priority:", priority[i])
        print("Time:", time[i])
        print("Reminder:", reminder[i])
        print("Reminder Time:", reminder_time[i])
        if reminder[i] == "Yes":

            print("Reminder Status:",
                "You have a task pending for", reminder_time[i])
        print("status:", status[i])
        print()

# TASK SUMMARY

print()
print(" TASK SUMMARY ")

print(" Total Tasks:", number)

completed = 0

for i in range(number):

    if status[i] == "Completed":
        completed=completed + 1

print("completed tasks:", completed)
print("pending tasks:", number - completed)     

# DELETE TASK

print()
print(" DELETE TASK ")

delete = int(input("which task do you want to delete"))

if delete >= 1 and delete <= number:
    tasks[delete - 1 ] = "Deleted" 
    status[delete - 1] = "Deleted"
    priority[delete - 1] = " Deleted"
    task_date[delete - 1] = "Deleted"
    time[delete - 1] = "Deleted"
    reminder[delete - 1] = "Deleted"
    reminder_time[delete - 1] = "Deleted"

    print(" TASK DELETED SUCCESSFULLY")

else:
    print("Invalid task number")

# TASK SUMMARY

print()
print(" TASK SUMMARY ")

print(" Total Tasks:", number)

completed = 0
pending = 0

for i in range(number):

    if status[i] == "Completed":
        completed=completed + 1

    if status[i] == "Pending":
        pending = pending + 1


print("Total Tasks:", completed + pending)
print("CompletedTtasks:", completed)
print("Pending Tasks:", pending)   

# TASK STATISTICS

print()
print("===== TASK STATISTICS =====")

active = 0
completed = 0
deleted = 0

for i in range(number):

    if status[i] == "Pending":
        active = active + 1

    if status[i] == "Completed":
        completed = completed + 1

    if status[i] == "Deleted":
        deleted = deleted + 1

print("Active Tasks:", active)
print("Completed Tasks:", completed)
print("Deleted Tasks:", deleted)

print()
show_statistics(status)

print("===== REMINDER SYSTEM =====")


current_time = datetime.now().strftime("%I:%M %p")

print("Current time:", current_time)

for i in range(number):

   
    if status[i] == "Pending" and reminder[i] == "Yes":

        
        if reminder_time[i].upper() == current_time:

            print()
            print("🔔 REMINDER")
            print("-------------------------")
            print("You have a task pending for",
                  reminder_time[i])
            print("Task:", tasks[i])
            print("Date:", task_date[i])
            print("Priority:", priority[i])
            print("-------------------------")

print()
print("Reminder check completed.")