from extension import mysqldb as db
from setting import config
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), index = True)
    password_hash = db.Column(db.String(128))

    def generate_auth_token(self, exprie=60):
        s = Serializer(config['SECRET_KEY'], expires_in=exprie)
        return s.dumps({'id':self.id})

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None
        user = User.query.get(data['id'])
        return user

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)
        return self.password_hash
        # self.password_hash = password

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
        # return  self.password_hash
