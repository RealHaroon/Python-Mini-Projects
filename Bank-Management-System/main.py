import json

# class BankAccount:
#     def __init__(self,acc_No,name,balance=0):
#         self.acc_No=acc_No
#         self.name=name
#         self.balance=balance

#     def deposit(self,amount):
#         if amount <=0:
#             print("Invalid Amount!")
#         else:
#             self.balance +=amount
#             print("Deposit Succesful.")

#     def withdraw(self,amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             print("Withdrawal succesful.")
#         else:
#             print("Insufficient balance or invalid amount")

#     def checkBalance(self):
#         return self.balance
    
#     def to_dict(self):
#         dic={ "Account Number":self.acc_No, "Name": self.name , "Balance":self.balance}
#         return dic


def getBalance(name,amount):
     file_path = "Bank-Management-System\\accounts.json"

    # Load existing accounts
     with open(file_path, "r") as file:
        accounts = json.load(file)

    # Update balance for the given user
     for account in accounts:
        if account["name"] == name:
            account["balance"] += amount
            break  # Stop loop after updating the correct user

    # # Save updated data back to the file
     with open(file_path, "w") as file:
        json.dump(accounts, file, indent=4)

        
        
print(getBalance("haroon",6000))

        


               




        