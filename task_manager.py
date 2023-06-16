# =====importing libraries=========
import os
from datetime import datetime, date

datetime_string_format = "%Y-%m-%d"

# Create tasks.txt if it doesn't exist.
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", 'w') as default_file:
        pass

with open("tasks.txt", 'r') as task_file:
    task_data = task_file.read().split("\n")
    task_data = [task for task in task_data if task != ""]

# Create list of dictionaries to contain tasks.
task_list = []
for task_string in task_data:
    current_task = {}

    # Split by semicolon and manually add each component.
    task_components = task_string.split(";")
    current_task['username'] = task_components[0]
    current_task['title'] = task_components[1]
    current_task['description'] = task_components[2]
    current_task['due_date'] = datetime.strptime(task_components[3], datetime_string_format)
    current_task['assigned_date'] = datetime.strptime(task_components[4], datetime_string_format)
    current_task['completed'] = True if task_components[5] == "Yes" else False
    
    task_list.append(current_task)

# ===Login Section===
'''This code reads usernames and passwords from the user.txt file to allow  a user to login.
'''
# If no user.txt file, write one with a default account.
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user data.
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary.
username_password = {}
for user in user_data:
    username, password = user.split(';')
    username_password[username] = password

logged_in = False
while not logged_in:
    print("LOGIN")
    current_user = input("Username: ")
    current_password = input("Password: ")
    if current_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[current_user] != current_password:
        print("Wrong password")
        continue
    else:
        print("Login successful!")
        logged_in = True

def reg_user():
    '''Function to add a new user to the user.txt file'''

# Allows user to add a new username while preventing user adding a duplicate name.
    while True:
        new_user = input("New username:\t")
        if new_user in username_password.keys():
            print("That name is already taken. Please enter a new username.")
            continue
        else:
            break
# Allows user to add a new password while preventing user adding duplicate.
    while True:
        new_password = input("New password:\t")
        if new_password in username_password.values():
            print("That password already exists. Please enter a new password.")
            continue
        else:
            break
    
    # Check if new password and confirmed password are the same.
    while True:
        confirm = input("Confirm password:\t")
        if confirm == new_password:
            break
        else:
            print("The passwords do not match.")
            continue
    
    # Confirm addition of new user.
    print("New user added.")
    username_password[new_user] = new_password
    
    # Write new user to user.txt file.
    with open("user.txt", "w") as out_file:
        user_data.append(f"{new_user};{new_password}")
        out_file.write("\n".join(user_data))


def add_task():
    '''Function to allow a user to add a new task to tasks.txt file
    Prompts a user for the following:
    - A username for the person whom the task is assigned to,
    -The title of the task,
    -A description of the task and
    -the due date of the task.'''
    
    # Get username of person task is assigned to.
    while True:
        user = input("Username of person assigned to task:\t")
        if user not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue
        else:
            break

    # Get title of task.
    task = input("Title of task:\t")
    # Get task description.
    task_description = input("Description of task:\t")
    
    # Get due date in correct format.
    while True:
        try:
            task_due_date = input("Due date of task (YYYY-MM-DD):\t")
            due_date_time = datetime.strptime(task_due_date, datetime_string_format)
            break
        except ValueError:
            print("Invalid datetime format. Please use the format specified")
    
    # Get today's date as date task assigned.
    current_date = date.today()

    # Add task to task in dictionary format to task_list.
    new_task = {
        "username": user,
        "title": task,
        "description": task_description,
        "due_date": due_date_time,
        "assigned_date": current_date,
        "completed": False
        }
    task_list.append(new_task)
    
    # Create list of values in task_list and convert to string to write to file. 
    task_list_to_write = []
    for t in task_list:
        string_attributes = [
        t["username"],
        t["title"],
        t["description"],
        t["due_date"].strftime(datetime_string_format),
        t["assigned_date"].strftime(datetime_string_format),
        "Yes" if t["completed"] else "No"
        ]
        task_list_to_write.append(";".join(string_attributes))

    # Write new task to file and notify user task added.
    with open("tasks.txt", "w") as task_file:
        task_file.write("\n\n".join(task_list_to_write))
    print("\nTask successfully added.")

def view_all():
    '''Function to display details of all tasks in specified format.'''
    for t in task_list:
        display_str = f"Task: \t\t\t {t['title']}\n"
        display_str += f"Assigned to: \t\t {t['username']}\n"
        display_str += f"Date Assigned: \t\t {t['assigned_date'].strftime(datetime_string_format)}\n"
        display_str += f"Due Date: \t\t {t['due_date'].strftime(datetime_string_format)}\n"
        display_str += f"Task Description:\t {t['description']}\n"
        print(display_str)

def view_mine():
    '''Function to enable users to view their assigned tasks in numbered format, confirm whether tasks have been completed, assign tasks to different user or change the due date.'''
    
    # Create list of tasks for current user.
    # Exclude completed tasks as these should not be edited.
    my_tasks = []
    for t in task_list:
        if t['username'] == current_user and t['completed'] == False:
            my_tasks.append(t)
    
    '''Reads the tasks from tasks.txt and prints to the console in the required format.'''
    for t in my_tasks:
        display_string = f"Task: \t\t {t['title']}\n"
        display_string += f"Assigned to: \t\t {t['username']}\n"
        display_string += f"Date Assigned: \t\t {t['assigned_date'].strftime(datetime_string_format)}\n"
        display_string += f"Due Date: \t\t {t['due_date'].strftime(datetime_string_format)}\n"
        display_string += f"Task Description: \t {t['description']}\n"
        # String to print to terminal with number addded at beginning.
        print(f"{my_tasks.index(t) + 1}. {display_string}")
    
    # List of numbers for user to enter to edit chosen task.
    t_numbers = []
    for i in my_tasks:
        task_number = my_tasks.index(i) + 1
        t_numbers.append(task_number)
    
    # Code to select task to edit or return to main menu.
    while True:
        try:
            edit_task = int(input("\nPlease input the number of the task you have completed or want to edit. If you want to return to the main menu, enter -1:\t"))
            if edit_task == -1:
                return
            else:
                edit_task in t_numbers
                break
        except ValueError:
            print("Enter the number assigned to one of your tasks.")
            continue
    
    # Subtract 1 from number of chosen task to obtain index of task in my_tasks.
    edit_task = edit_task -1
    target_task = my_tasks[edit_task]
    title_value = target_task['title']
    
    # Find matching task_list value in my_tasks.
    # Adapted from geeksforgeeks https://www.geeksforgeeks.org/python-find-dictionary-matching-value-in-list/ 
    target_dict = None
    for dict in task_list:
        if dict ['title'] == title_value:
            target_dict = dict
            break
    
    task_completed = input("Is this task completed? Please type in Yes or No:\t")
    # Ensure input is title case.
    task_completed = task_completed.title()
    if task_completed == 'Yes':
        target_dict['completed'] = True
    else:
        print("Please input a different username for this task or enter a new due date using the correct format.")
        choice = int(input("Enter 1 to change the user or 2 to change the due date:\t\t"))
        
        # Assign a different user to task.
        if choice == 1:
            edit_user = input("Please enter a new user:\t")
            target_dict['username'] = edit_user
        
        # Change due date making sure to use correct date format.
        else:
            while True:
                try:
                    edit_duedate = input("Please enter a new due date with the correct format:\t\t")
                    target_dict['due_date'] = datetime.strptime(edit_duedate, datetime_string_format)
                    break
                except ValueError:
                    print("Invalid datetime format. Please use the format specified")
    
    # Write updated values to tasks.txt
    task_list_to_write = []
    for t in task_list:
        string_attributes = [
        t["username"],
        t["title"],
        t["description"],
        t["due_date"].strftime(datetime_string_format),
        t["assigned_date"].strftime(datetime_string_format),
        "Yes" if t["completed"] else "No"
        ]
        task_list_to_write.append(";".join(string_attributes))
    with open("tasks.txt", "w") as task_file:
        task_file.write("\n\n".join(task_list_to_write))


def gen_reports():
    '''Function to create 2 new text files, task_overview.txt and user_overview.txt. the first contains the total number of completed tasks, the total number of uncompleted tasks and the total number of uncompleted tasks that are overdue in addition to the percentages of uncompleted and overdue tasks. The second contains, for each user, the total number of tasks assigned, the percentage of tasks assigned and the percentages for completed tasks, uncompleted tasks and overdue tasks.''' 

    # Create the text files.
    with open("task_overview.txt", "w") as default_file:
        pass
    with open("user_overview.txt", "w") as default_file:
        pass
    
    # Import timedelta form datetime.
    from datetime import timedelta

    # Create list of usernames and variable for number of tasks.
    user_list = list(username_password.keys())
    total_tasks = len(task_list)
    
    # Create list and get number of completed tasks.
    completed_tasks = []
    for t in task_list:
        if t['completed'] == True:
            completed_tasks.append(t)
    total_completed = len(completed_tasks)
    
    # Create list and get number of uncompleted tasks.
    uncompleted_tasks = []
    for t in task_list:
        if t['completed'] == False:
            uncompleted_tasks.append(t)
    total_uncompleted = len(uncompleted_tasks)
    
    # Create list and get number of overdue tasks.
    overdue_tasks = []
    # I discovered that where the due date was the same as the current date, the program marked the tasks as overdue.
    # By using timedelta to subtract 1 day from current_date, I could surmount this problem.
    current_date = datetime.today() - timedelta(days=1)
    for t in task_list:
        if t['due_date'] < current_date and t['completed'] == False:
            overdue_tasks.append(t)
    total_overdue = len(overdue_tasks)
    
    # Code to calculate percentages and round them to integers.
    perc_incomplete = total_uncompleted/total_tasks * 100
    perc_incomplete = round(perc_incomplete)
    perc_overdue = total_overdue/total_tasks * 100
    perc_overdue = round(perc_overdue)
    
    # Write numbers and percentages to file and display in console.
    with open("task_overview.txt", "w+") as task_report:
        task_report.write("\nTASK OVERVIEW\n\n")
        task_report.write(f"Total number of tasks:\t{total_tasks}")
        task_report.write(f"\nNumber completed :\t{total_completed}")
        task_report.write(f"\nNumber uncompleted:\t{total_uncompleted}")
        task_report.write(f"\nNumber overdue:\t\t{total_overdue}")
        task_report.write(f"\nPercentage incomplete:\t{perc_incomplete}%")
        task_report.write(f"\nPercentage overdue:\t{perc_overdue}%\n")
    
    # Calculate number of tasks assigned to each user.
    # Create list of tasks by username assigned to task.
    user_tasks = []
    for t in task_list:
        user_tasks.append(t['username'])
    
    # Import counter to get number of tasks per user.
    from collections import Counter
    assigned_task = Counter(user_tasks)
    
    # Create list of number of tasks per user.
    assigned_tasks = []
    for i in range(0, len(user_list)):
        assigned_task[user_list[i]]
        assigned_tasks.append(assigned_task[user_list[i]])
    
    # Create list of percentage of tasks per user.
    perc_assigned_tasks = []
    for i in range(0, len(user_list)):
        perc_assigned_task = assigned_tasks[i]/total_tasks * 100
        perc_assigned_task = round(perc_assigned_task)
        perc_assigned_tasks.append(perc_assigned_task)

    # Create list of completed tasks per user.
    user_comp_tasks = []
    for t in completed_tasks:
        user_comp_tasks.append(t['username'])
    
    # Use counter to get number of completed tasks per user.
    comp_task = Counter(user_comp_tasks)
    # Use counter to get number of all tasks per user.
    user_total_tasks = Counter(user_tasks)
    
    # New list for percentage of completed tasks per user.
    perc_user_complete = []
    # Calculate percentage of completed tasks per user, round to integer and add to list.
    for x in comp_task:
        perc_complete = comp_task[x]/user_total_tasks[x] * 100
        perc_complete = round(perc_complete)
        perc_user_complete.append(perc_complete)
    
    # Eliminate duplicate usernames from list.
    user_comp_tasks = list(dict.fromkeys(user_comp_tasks))
    # Create dictionary of users and percentages of completed tasks.
    perc_comp_dict = dict(zip(user_comp_tasks, perc_user_complete))
    
    # Create dictionary of all users with 0 for value.
    user_comp_perc ={}
    for i in user_list:
        user_comp_perc[i] = 0
    # Merge dictionaries and convert to list for final output. 
    user_comp_perc.update(perc_comp_dict)
    completed = list(user_comp_perc.values())

    # Repeat procedure above for uncompled tasks.
    user_uncomp_tasks = []
    for t in uncompleted_tasks:
        user_uncomp_tasks.append(t['username'])
    uncomp_task = Counter(user_uncomp_tasks)
    user_total_tasks = Counter(user_tasks)
    perc_user_uncomplete = []
    for x in uncomp_task:
        perc_uncomplete = uncomp_task[x]/user_total_tasks[x] * 100
        perc_uncomplete = round(perc_uncomplete)
        perc_user_uncomplete.append(perc_uncomplete)
    user_uncomp_tasks = list(dict.fromkeys(user_uncomp_tasks))
    perc_uncomp_dict = dict(zip(user_uncomp_tasks, perc_user_uncomplete))
    user_uncomp_perc = {}
    for i in user_list:
        user_uncomp_perc[i] = 0
    user_uncomp_perc.update(perc_uncomp_dict)
    uncompleted = list(user_uncomp_perc.values())

    # Repeat procedure above for overdue tasks.
    user_overdue_tasks = []
    for t in overdue_tasks:
        user_overdue_tasks.append(t['username'])
    overdue_task = Counter(user_overdue_tasks)
    user_total_tasks = Counter(user_tasks)
    perc_user_overdue = []
    for x in overdue_task:
        perc_overdue = overdue_task[x]/user_total_tasks[x] * 100
        perc_overdue = round(perc_overdue)
        perc_user_overdue.append(perc_overdue)
    user_overdue_tasks = list(dict.fromkeys(user_overdue_tasks))
    perc_overdue_dict = dict(zip(user_overdue_tasks, perc_user_overdue))
    user_overdue_perc = {}
    for i in user_list:
        user_overdue_perc[i] = 0
    user_overdue_perc.update(perc_overdue_dict)
    overdue = list(user_overdue_perc.values())
    
    # Combine final lists from previous stages into new list.
    user_stats = []
    user_stats.append(user_list)
    user_stats.append(assigned_tasks)
    user_stats.append(perc_assigned_tasks)
    user_stats.append(completed)
    user_stats.append(uncompleted)
    user_stats.append(overdue)

    # List of lists for final output to file.
    stats_to_print = []
    for i in range(0, len(user_list)):
        stats_to_print.append([])

    # Loop to generate lists of users with apposite numbers.
    for i in user_stats:
        n = 0
        for n in range(0, len(stats_to_print)):
            stats_to_print[n].append(i[n])
            n += 1

    # Number of users to write to file.
    total_users = len(user_data)

    # Write information to file.
    with open("user_overview.txt", "w+") as user_report:
        user_report.write("\n\nUSER OVERVIEW\n")
        user_report.write(f"\nNumber of Users:\t{total_users}\n")
        user_report.write(f"Number of tasks:\t{total_tasks}\n\n")
        # String formatted to act as column headings.
        # The spacing will depend on the number of characters in the usernames.
        user_report.write("\nUsername\tNo. tasks\t% tasks\t\t% completed\t% uncompleted\t% overdue\n\n")
        # Loop to write strings formatted as rows.
        for i in stats_to_print:
            i = "\t\t".join(map(str, i))
            user_report.write(i + "\n")

       
while True:
    # Presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    menu = input('''Select one of the following options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - View my task
    gr - Generate reports
    ds - Display statistics
    e - Exit
    :\t''').lower()

    # Execute menu commands.

    if menu == "r" and current_user == "admin":
        add_user = reg_user()

    elif menu == "a" and current_user == "admin":
        new_task = add_task()

    elif menu == "va":
        view_tasks = view_all()

    elif menu == "vm":
        my_assigned_tasks = view_mine()

    elif menu == "gr" and current_user == "admin":
        reports = gen_reports()

    elif menu == "ds" and current_user == "admin":
        with open("task_overview.txt", "r") as file:
            content = file.read()
            print(content)

        with open("user_overview.txt", "r") as file:
            content = file.read()
            print(content)

    elif menu == "e":
        print("Goodbye!")
        exit()

    else:
        print("You have made a wrong choice. Please try again.")

    





