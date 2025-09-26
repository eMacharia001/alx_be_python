# daily_reminder.py

# Loop to make sure the user provides valid inputs
while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Use match case for priority handling
    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Note: '{task}' is a low priority task"
        case _:
            print("Invalid priority entered. Please try again.\n")
            continue  # restart loop if invalid priority

    # Add time-bound condition
    if time_bound == "yes":
        reminder += " that requires immediate attention today!"
    else:
        if priority == "low":
            reminder += ". Consider completing it when you have free time."

    # Print the final customized reminder
    print(reminder)
    break  # exit after one valid reminder

