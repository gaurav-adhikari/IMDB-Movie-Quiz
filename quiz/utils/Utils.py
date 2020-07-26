import random
from quiz import bcrypt

def generatePasswordHash(userPasswordPlain):
    
    """
    Returns hashed password by converting the given plain text
    :param userPasswordPlain: hash password of the given user
    :type string
    """

    hashedPassword = bcrypt.generate_password_hash(
        userPasswordPlain).decode('utf-8')
    return hashedPassword


def checkPasswordHash(userHashedPassword, enteredPassword):

    """
    Returns true if the given plain text is equal to hashed text

    :param userHashedPassword: hash password of the given user
    :type string
    :param userHashedPassword: plain password entered by the user
    :type string

    :returns boolean value if both the hashes match
    :type boolean
    """

    return bcrypt.check_password_hash(userHashedPassword, enteredPassword)


def generateReferral():
    
    """
    Generates a random and unique referal code of 5 characters

    :returns referralCode 
    :type string
    """

    charSet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    referralCode = ''
    for i in range(0, 5):
        subStart = random.randint(0, len(charSet) - 1)
        referralCode += charSet[subStart: subStart + 1]

    return referralCode


def generateDummyTestQuestions():
   
    """
    Function to generate dummy quiz Questions
    """

    for i in range(1, 11):
        i = str(i)
        q = Questions(question="question"+i, choice1="q"+i+"C"+"1", choice2="q" +
                      i+"C"+"2", choice3="q"+i+"C"+"3", choice4="q"+i+"C"+"4", correctAnswer=i)
        try:    
            db.session.add(q)
            db.session.commit()
            
        except Exception as e:
            print(e)