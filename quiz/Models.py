from quiz import db


class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
    recentScore = db.Column(db.Integer)

    def __repr__(self):
        return f"'UserInfo('{self.username}','{self.email}','{self.recentScore}')'"


# TODO schema for Questions
class QuestionsSchema(db.Model):
    pass
