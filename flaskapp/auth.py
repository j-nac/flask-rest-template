from flaskapp import db
from flaskapp.models import User
from datetime import datetime

def authenticate(username, password):
    user = db.session.execute(db.select(User).filter_by(email=username)).scalar()
    if user and user.check_password(password.encode('utf-8')):
        user.last_login_timestamp = datetime.now()
        db.session.commit()
        return user

def identity(payload):
    user_id = payload['identity']
    return db.session.get(User, user_id)