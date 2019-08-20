from flask import jsonify, g
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()


@auth.get_password
def get_password(username):
    # 提供默认密码 会被前段上送密码覆盖
    if username == 'ok':
        return 'python2'
    return None


@auth.verify_password
def verify_password(username_or_token, password):
    from apps.user.model import User

    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True


@auth.error_handler
def unauthorized():
    return jsonify({'error': 'Unauthorized access'}), 403