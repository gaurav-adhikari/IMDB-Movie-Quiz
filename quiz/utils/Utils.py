import random
from quiz import bcrypt

def generatePasswordHash(userPasswordPlain):
    hashedPassword=bcrypt.generate_password_hash(userPasswordPlain).decode('utf-8')
    return hashedPassword
    
def checkPasswordHash(userHashedPassword,enteredPassword):
    return bcrypt.check_password_hash(userHashedPassword,enteredPassword)

def generateReferral():
    charSet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    referralCode = ''
    for i in range(0, 5):
        subStart = random.randint(0, len(charSet) - 1)
        referralCode += charSet[subStart: subStart + 1]

    return referralCode
