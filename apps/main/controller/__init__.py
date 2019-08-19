from apps.main import bp
from flask import render_template

@bp.route('/a')
def index():
    return render_template('index.html')
