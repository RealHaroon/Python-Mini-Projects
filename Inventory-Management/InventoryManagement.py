
inventory={}
while True:
 print(" \tMy Inventory Management System \n")
 print("1,Add Product")
 print("2,Update Pricing")
 print("3,Display All Product")
 print("4,Exit")

 inp1=input("Enter your choice between 1-4 : ")
 if inp1=="1":
   print("\tAdd Product")
   addPro=input("Enter Name of Product: ")
   addPrice=float(input("Enter The Price of Product: "))
   inventory.update({addPro:addPrice})
   print(f"Product: {addPro} added with Price:{addPrice}. ")
 if inp1=="2":
  print("\tUpdate Price of Existing Product: ")
  addPro=input("Enter Name of Product: ")
  addPrice=float(input("Enter New The Price of Product: "))
  inventory.update({addPro:addPrice})
  print(f"Product: {addPro}  Price:{addPrice} Updated. ")
 if inp1=="3":
  name=inventory.keys()
  price=inventory.values()
  if len(inventory)==0:
   print("Inventory has no Product!")
  else:
     print("\tAll Products with Price")
 for name, price in inventory.items():
     print(f'"Name": {name} "Price": {price}')
 if inp1=="4":
    print("Exited!")
    break