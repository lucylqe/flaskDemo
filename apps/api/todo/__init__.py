from apps.api.todo.resources import todo
resource_map = [{

    'version':'v1.0',
    'prefix':'todo',
    'resources':[
        (todo.TodoList, '/todos'),
        (todo.Todo, '/todos/<todo_id>'),
    ]
}]