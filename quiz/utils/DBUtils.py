""" Database Utilities """

from quiz import db
from quiz.Models import UserInfo

from quiz.utils.Utils import generatePasswordHash

def adminEntryCheckHelper():
    "Checks if the user 'admin' is added to the DB , if not Adds admin to the DB"

    if UserInfo.query.filter_by(username="admin").first() == None:
        adminUser = UserInfo(username="admin", password=generatePasswordHash(
            "admin"), email="admin@admin.com", referralCode="admin")
        try:
            db.session.add(adminUser)
            db.session.commit()
        except:
            db.rollback()

