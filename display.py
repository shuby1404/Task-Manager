def show_tasks(tasks, task_date, priority, status, time, reminder, reminder_time):

    print("YOUR TASKS")

    for i in range(len(tasks)):
        print(i + 1, ".", tasks[i])
        print("Date:", task_date[i])
        print("Priority:", priority[i])
        print("Time:", time[i])
        print("Reminder:", reminder[i])
        print("Reminder Time:", reminder_time[i])
        print("Status:", status[i])
        print()
