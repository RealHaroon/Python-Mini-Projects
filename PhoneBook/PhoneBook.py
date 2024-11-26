contacts={}
while True:
 print("\t\t\tMy PhoneBook\n")
 print("1,Add Contact ")
 print("2,Delete Contact ")
 print("3,Display All Contact ")
 print("4, Exit")
 inp=input("\n\nChoose in 1-4 : ")
 if inp=="1":
  addName=input("Enter Name : ")
  addNum=int(input("Enter Number : "))
  contacts.update({addName:addNum})
 elif inp=="2":
  popCont=input("Enter the Name of contact you wanna delete : ")
  contacts.pop(popCont)
 elif inp=="3":
  print("All Contact\n")
  print(contacts)
 elif inp=="4":
  break