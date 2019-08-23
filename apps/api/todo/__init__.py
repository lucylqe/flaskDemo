from apps.api.todo.resources import todo
resource_map = [{
    'version':'v1.0',
    'name':'',
    'resources':[ todo.TodoList, todo.Todo ]
}]

