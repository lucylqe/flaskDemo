from extension import api
from apps.api import blog
from apps.api import login

api.add_resource(login.HelloWorld, '/hello')
