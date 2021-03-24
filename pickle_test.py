import pickle


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

with open(".todo.pickle", "rb") as f:
    loaded = pickle.load(f, encoding = "latin1")
    print(loaded)