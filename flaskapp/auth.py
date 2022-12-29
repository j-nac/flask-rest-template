from flaskapp import db
from flaskapp.models import User

def authenticate(username, password):
    user = db.first_or_404(db.select(User).filter_by(email=username))
    if user.check_password(password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return db.get_or_404(User, user_id)