class CRUD:
    def __init__(self,items):
        self.items=items
    def addEntry(self,entry):
        self.items.append(entry)
    def removeEntry(self,entryId):
        if any(item['id'] == entryId for item in self.items):
         self.items=[item for item in self.items if item['id']!=entryId]
        else:
           print("Entry doesnt exist!")
    def editEntry(self,entryId,newEntry):
        for i,item in enumerate(self.items):
          if item['id']==entryId:
              self.items[i]=newEntry
              return True
        return False
    def printEntry(self):
       for item in self.items:
          print(item)
            


items=[
        {'id':1,'name':'Phone','model':'IPhone 11','price':500},
        {'id':2,'name':'Laptop','model':'Macbook','price':999},
        {'id':3,'name':'Keyborad','model':'HXZ1122','price':49}
    ]
crud=CRUD(items)
while True:
    print("1. Add Entry")
    print("2. Remove Entry")
    print("3. Edit Entry")
    print("4. Print Entries")
    print("5. Exit")
    inp=input("Enter Your Choice (1-5): " )
    if inp=='1':
       id_=int(input("Enter Id: "))
       name=input("Enter name : ")
       model=input("Enter Model : ")
       price=int(input("Enter Price : "))
       newEntry={
          'id':id_,'name':name,'model':model,'price':price}
       crud.addEntry(newEntry)
    elif inp=='2':
       id_=int(input("Enter Id to delete entry : "))
       crud.removeEntry(id_)
    elif inp =='3':
       id_=int(input("Enter Id to Edit entry :"))
       name=input("Enter new name : ")
       model=input("Enter new Model : ")
       price=int(input("Enter new Price : "))
       newEntry={
          'id':id_,'name':name,'model':model,'price':price}
       if not crud.editEntry(id_,newEntry):
          print("Entry Not Found")
    elif inp=='4':
       crud.printEntry()
    elif inp=='5':
       print("bye")
       break
    else:
       print("Invalid Input")