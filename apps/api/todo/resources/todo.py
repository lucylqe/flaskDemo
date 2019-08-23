from flask_restful import reqparse, Resource, abort
from flask_restful import fields, marshal_with, marshal

from apps.api.todo.models.todo import TodoModel
from apps.auth import auth

TODOS = {
    'todo1': TodoModel(todo_id='todo1', title='看书', desc='盗墓笔记'),
    'todo2': TodoModel(todo_id='todo2', title='打游戏', desc='玩王者荣耀'),
    'todo3': TodoModel(todo_id='todo3', title='吃饭', desc='吃泡面'),
}

resource_fields = {
    'task': {
        'id': fields.String(attribute='todo_id'),
        'title': fields.String(attribute='title'),
        'description': fields.String(attribute='desc'),
    },
    'uri': fields.Url('todo')
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))


parser = reqparse.RequestParser()
parser.add_argument('title', type=str, nullable=True)
parser.add_argument('desc', type=str, nullable=True)

put_parser = parser.copy()
put_parser.replace_argument('title', required=True)


class Todo(Resource):
    urls = ['//todos/<todo_id>']

    @auth.login_required
    @marshal_with(resource_fields)
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def post(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        args = parser.parse_args()
        title = args['title']
        desc = args['desc']
        task = {}
        if title is not None:
            TODOS[todo_id].title = task['title'] = title
        if desc is not None:
            TODOS[todo_id].desc = task['desc'] = desc
        return task, 201

    def put(self, todo_id):
        args = put_parser.parse_args()
        title = args['title']
        desc = args['desc']
        TODOS[todo_id] = task = TodoModel(todo_id, title=title, desc=desc)
        return marshal(task, resource_fields), 201

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204


class TodoList(Resource):
    urls = ['//todos']

    def get(self):
        return [marshal(todo, resource_fields) for todo in TODOS.values()]