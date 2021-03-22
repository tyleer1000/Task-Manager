#https://www.tutorialspoint.com/python/python_classes_objects.htm
#https://docs.python.org/3/whatsnew/3.6.html#pep-498-formatted-string-literals
#https://docs.python.org/3/tutorial/classes.html
#https://thewhitetulip.gitbooks.io/build-applications-in-python-the-anti-textbook/content/manuscript/10-task.html
#https://www.programiz.com/python-programming/class
#https://gobyexample.com/command-line-arguments#:~:text=Command%2Dline%20arguments%20are%20a,to%20parameterize%20execution%20of%20programs.&text=Args%20provides%20access%20to%20raw,the%20arguments%20to%20the%20program.
#https://www.pythoncentral.io/how-to-pickle-unpickle-tutorial/

import pickle
from datetime import date
import sys
args = sys.argv
tasks = []
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



#Requires user to enter a command
try:
    command = args[1]
except IndexError:
    print("Choose a command!")
    sys.exit(1)

#ensures that the user enters a valid command from the list of possible commands
if command not in (add,remove,list,report,done):
    print("Invalid command\n Use {0}/{1}/{2}/{3}/{4}/{5}".format(add,remove,list,report,done))
    sys.exit(1)
#creates a task object with inputted attributes and adds it to a pickled file 
if command == "add":
    t = Task()
    t.id = args[2]
    t.name = args[3]
    t.created = date.today()
    t.due = args[4]
    tasks.append(t)
    with open(".todo.pickle", "a") as f:
        pickle.dump(tasks, f)

elif command == "remove":
    file = open("tasks.txt", "r")
    tasks = file.readlines()
    tasks = [task.strip() for task in tasks]
    task_id = args[2]
    del tasks[int(task_id)]

    file = open("tasks.txt", "w")
    tasks = [task + "\n" for task in tasks]
    file.writelines(tasks)


elif command == "list":
    file = open("tasks.txt", "r")
    tasks = file.readlines()
    if len(tasks) == 0:
        print("there are no tasks!")
    else:
        print("|-----{0}----{1}----|".format("title", "content"))
        tasks = [task.strip() for task in tasks]
        for task in tasks:
            title, content = task.split('|')
            print("{0} {1}".format(title, content))
            file.close()
else:
    print("invalid command!")

with open(".todo.pickle", "rb") as f:
    test = pickle.load(f)
    for t in test:
        print(t.name)

for t in tasks:
    print t.id