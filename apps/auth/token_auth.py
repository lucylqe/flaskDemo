from flask import g, jsonify

from apps.auth.base_auth import auth
from apps.auth import bp

@bp.route('/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({'token':token.decode('ascii')})