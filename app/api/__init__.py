
from app.api.blog import blueprint as blog_blueprint
from app.api.login import blueprint as login_blueprint

from app.libs.register_blueprint import NestableBlueprint

blueprint = NestableBlueprint(__name__, __name__)
blueprint.register_blueprint(blog_blueprint, url_prefix='/blog')
blueprint.register_blueprint(login_blueprint, url_prefix='/login')

@blueprint.route('/')
def test():
    return str(__name__)