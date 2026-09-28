def set_reminder(reminder, reminder_time, i, tasks):

    choice = int(input("Do you want a reminder? "))

    if choice == 1:
        reminder[i] = "Yes"

        reminder_time[i] = input("Enter reminder time (HH:MM): ")

        am_pm = input("Enter AM or PM: ")
        am_pm = am_pm.upper()

        if am_pm == "AM" or am_pm == "PM":
            reminder_time[i] = reminder_time[i] + " " + am_pm
        else:
            print("Invalid AM/PM choice.")
            reminder_time[i] = reminder_time[i] + " AM"

    elif choice == 2:
        reminder[i] = "No"
        reminder_time[i] = "NO reminder"

    else:
        reminder[i] = "No"
        reminder_time[i] = "NO reminder"
        print("Invalid reminder choice.")

    return reminder, reminder_time


