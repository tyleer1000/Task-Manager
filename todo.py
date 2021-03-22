#https://www.tutorialspoint.com/python/python_classes_objects.htm
#https://docs.python.org/3/whatsnew/3.6.html#pep-498-formatted-string-literals
#https://docs.python.org/3/tutorial/classes.html
#https://thewhitetulip.gitbooks.io/build-applications-in-python-the-anti-textbook/content/manuscript/10-task.html
#https://www.programiz.com/python-programming/class
#https://gobyexample.com/command-line-arguments#:~:text=Command%2Dline%20arguments%20are%20a,to%20parameterize%20execution%20of%20programs.&text=Args%20provides%20access%20to%20raw,the%20arguments%20to%20the%20program.
#https://www.pythoncentral.io/how-to-pickle-unpickle-tutorial/

import pickle
import os.path
from os import path
from datetime import date
import sys
args = sys.argv

#creates list of valid commands
add,remove,list,report,done = "add","remove","list","report","done"

class Task:
    """Representation of a task Attributes:
    -created date
    -completed date
    -name 
    -ID
    -priority (1,2 or 3. optional)
    """

    def __init___(self, id, name, created, due, priority, completed):
        self.id = id
        self.name = name
        self.created = created
        self.due = due
        self.priority = priority
        self.completed = completed


#list of tasks. This should be generated from the .todo.pickle file if the file has been created by the user
tasks = []
#list of complete tasks
complete_tasks = []
#checks if the user has created any tasks, and unpickles those tasks and reads them into the task list
if path.exists(".todo.pickle"):
    with open(".todo.pickle", "rb") as f:
        existing_tasks = pickle.load(f)
        for t in existing_tasks:
            tasks.append(t)

#Requires user to enter a command
try:
    command = args[1]
except IndexError:
    print("Choose a command!")
    sys.exit(1)

#ensures that the user enters a valid command from the list of possible commands
if command not in (add,remove,list,report,done):
    print("Invalid command\n Use {0}/{1}/{2}/{3}/{4}".format(add,remove,list,report,done))
    sys.exit(1)
#creates a task object with inputted attributes and adds it to a pickled file 
if command == "add":
    t = Task()
    t.id = args[2]
    t.name = args[3]
    t.created = date.today()
    t.due = args[4]
    tasks.append(t)
    #pickles the new task and appends it to the pickle file
    with open(".todo.pickle", "a") as f:
        pickle.dump(tasks, f)

#removes a task from the task list and re-writes the pickle file
elif command == "remove":
    #removes a task from the task list based on the id # of the task
    tasks.pop(args[2])
    #over writes the pickle file with the shortened task list
    with open(".todo.pickle", "w") as f:
        pickle.dump(tasks, f)

#reads the pickle file into a new list and prints out that list for the user to view the existing tasks
elif command == "list":
    with open(".todo.pickle", "rb") as f:
        existing_tasks = pickle.load(f)
        for t in existing_tasks:
            print(t)

elif command == "done":
    #removes a task from the task list based on the id # of the task
    done_task = tasks.pop(args[2])
    #appends the task to the completed task list
    complete_tasks.append(done_task)
    #over writes the pickle file with the new task list and complete task list
    with open(".todo.pickle", "w") as f:
        pickle.dump(tasks, f)


else:
    print("invalid command!")

