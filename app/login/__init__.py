from flask import Blueprint
blueprint = Blueprint(__name__, __name__)

@blueprint.route('/')
def test():
    return str(__name__)