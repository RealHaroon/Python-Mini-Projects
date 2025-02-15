class Cafe: # Cafe class
 total=0 # class attribute 
 
 def printMenu(self,menu): # Print Menu
    print("**Items : Prices**\n")
    for k,v in menu.items():
        print(f"{k} : Rs{v}")
 
 def takeOrder(self,menu): # Take Order 
    inp_item=input("Enter The Name of item you want to order= ").lower()
    if inp_item in menu:
       self.total+=menu[inp_item]
       print(f"Your item {inp_item}  has been added to you order.")
    else:
       print(f"{inp_item} is not avaiable yet!")
 
 def printTotal(self) ->int: # get Total
    return self.total
    
    

menu={  # Menu
    "biriyani":150,
    "samosa":20,
    "tea":50,
    "pattie":30,
    "coffee":50,
    "cold drink":60,
    "roll":30,
    "burger":70

}

ordr= Cafe() # order obj
ordr.printMenu(menu)
ordr.takeOrder(menu)
while True:
   inp=input("Do you want to order more? (Yes/No)").lower()
   if inp == "yes":
      ordr.takeOrder(menu)
   else:
      break

total=ordr.printTotal()
print("Your Total bill = Rs",total)

  


