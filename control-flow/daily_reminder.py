# task_reminder.py

# Prompt user for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process task based on priority
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Add time-bound condition
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    elif priority == "medium":
        reminder += ". Try to schedule it soon."
    elif priority == "high":
        reminder += ", but it is not urgent today."

# Display final reminder
print("\n" + reminder)

