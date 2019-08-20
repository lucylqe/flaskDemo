class TodoModel:
    def __init__(self, todo_id, title, desc):
        self.todo_id = todo_id
        self.title = title
        self.desc = desc
        self.done = False