import random

class Utils:

    def generateReferral():
        charSet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        referralCode = ''
        for i in range(0, 5):
            subStart = random.randint(0, len(charSet) - 1)
            referralCode += charSet[subStart: subStart + 1]

        return referralCode
