from flask import Blueprint, redirect, url_for

blueprint = bp = Blueprint(__name__, __name__)


@bp.route('/')
def index():
    return redirect(url_for('main.index'))


@bp.route('/favicon.ico')
def ico():
    return redirect(url_for('static', filename='favicon.ico'))

