from flask import render_template
from apps.libs.register_blueprint import NestableBlueprint
blueprint = bp = NestableBlueprint(cur_name=__name__, cur_file=__file__)

from .base_auth import auth
from .token_auth import get_auth_token