from apps.libs.register_blueprint import NestableBlueprint

from apps.api.blog import bp as blog_blueprint
from apps.api.login import bp as login_blueprint


blueprint = bp = NestableBlueprint(cur_name=__name__,cur_file=__file__)
blueprint.register_blueprint(blog_blueprint, url_prefix='/blog')
blueprint.register_blueprint(login_blueprint, url_prefix='/login')

@bp.route('/')
def index():
    return str(__name__)
