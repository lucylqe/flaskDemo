from apps.main import bp
from flask import render_template

@bp.route('/a')
def a():
    return render_template('index.html')
