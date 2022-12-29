from flaskapp import db
from flaskapp.models import User
from datetime import datetime

def authenticate(username, password):
    user = db.one_or_404(db.select(User).filter_by(email=username))
    if user.check_password(password.encode('utf-8')):
        user.last_login_timestamp = datetime.now()
        db.session.commit()
        return user

def identity(payload):
    user_id = payload['identity']
    return db.one_or_404(User, user_id)