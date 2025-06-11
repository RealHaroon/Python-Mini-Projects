import random
import string
class PasswordGenerator:
    def generatePassword(self,addUpperCase,addLowerCase,addDigits,addSpecialChar):
        passWord=[]
        charPool=''
        
        if addUpperCase:
                passWord.append(random.choice(string.ascii_uppercase))
                charPool += string.ascii_uppercase
        if addLowerCase:
                passWord.append(random.choice(string.ascii_lowercase))
                charPool += string.ascii_lowercase
        if addDigits:
                passWord.append(random.choice(string.digits))
                charPool += string.digits
        if addSpecialChar:
                passWord.append(random.choice(string.punctuation))
                charPool += string.punctuation
        
        if not charPool:
               return "Error! no type selected."

        while len(passWord) < 12:
            passWord.append(random.choice(charPool))
        
        random.shuffle(passWord)
        return ''.join(passWord)

obj=PasswordGenerator()
addUpper=input("Add UpperCase Letters ? (y/n):")=='y'
addLower=input("Add LowerCase Letters ? (y/n): ")=='y'
addDigit=input("Add Digits ? (y/n): ") =='y'
addSpecial=input("Add Special Characters ? (y/n): ")=='y'

strongPassword=obj.generatePassword(addUpper,addLower,addDigit,addSpecial)
print("Generated Strong Password",strongPassword)
