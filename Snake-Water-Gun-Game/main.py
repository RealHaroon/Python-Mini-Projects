'''
1 for snake
-1 for water
0 for gun
'''
import random


computer=random.choice([-1,0,1])
youStr=input("Enter Your Choice")
youDict={"s":1,"w":-1,"g":0}
reversDict={1:"snake",-1:"water",0:"gun"}
you=youDict[youStr]
print(f" You chose {reversDict[you]} \n Computer chose {reversDict[computer]}")

if(computer==you):
    print("Draw")
else:
 if(computer==-1 and you==1):
    print("You Win")
 elif(computer == -1 and you==0):
    print("You Lose")
 elif(computer==1 and you==-1):
    print("You Lose")
 elif(computer==1 and you ==0):
    print("You Win")
 elif(computer==0 and you==-1):
    print("You Win")
 elif(computer==0 and you ==1):
    print("You Lose")
 else:
    print("Something went wrong")