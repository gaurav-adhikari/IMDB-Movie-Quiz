from quiz import db,loginManager
from flask_login import UserMixin

db.create_all()

@loginManager.user_loader
def loadUser(userID):
    return UserInfo.query.get(int(userID))


class UserInfo(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    recentScore = db.Column(db.Integer,default=0)
    # referralCode = db.Column(db.String(256),nullable=True)


    def __repr__(self):
        return f"'UserInfo('{self.username}','{self.email}','{self.password}','{self.recentScore}')'"
        
# TODO schema for Questions
