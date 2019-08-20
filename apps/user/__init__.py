from apps.libs.register_blueprint import NestableBlueprint
blueprint = bp = NestableBlueprint(cur_name=__name__,cur_file=__file__)


@bp.route('/')
def index():
    return str(__name__)