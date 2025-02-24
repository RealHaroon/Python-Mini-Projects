import json
import os


class BankAccount:
    def __init__(self,acc_No,name,balance=0):
        self.acc_No=acc_No
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        if amount <=0:
            print("Invalid Amount!")
        else:
            self.balance +=amount
            print("Deposit Succesful.")

    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawal succesful.")
        else:
            print("Insufficient balance or invalid amount")

    def checkBalance(self):
        return self.balance
    
    def to_dict(self):
        dic={ "Account Number":self.acc_No, "Name": self.name , "Balance":self.balance}
        return dic

class Bank:
    def __init__(self):
        self.filePath="Bank-Management-System\\accounts.json"

    
    def createAccount(self,name,accountNo):
        if os.path.exists(self.filePath) and os.path.getsize(self.filePath) > 0:
            with open(self.filePath, "r") as file:
                try:
                    accounts = json.load(file)
                except json.JSONDecodeError:
                    accounts = []  # If file is empty or corrupted
        else:
            accounts = []
        
        for account in accounts:
            if account["accountNo"] == accountNo:
                return f"Account with account number {accountNo} already exists"
        
        new_account={
                    "name":name,
                    "accountNo":accountNo,
                    "balance": 0

                }

        accounts.append(new_account)

        with open(self.filePath, "w") as file:
            json.dump(accounts, file, indent=4)
        return f"Account for {name} (Account No: {accountNo}) created successfully."


name=input("Enter your name")
accNo=int(input("Enter account number"))
user=Bank()
user.createAccount(name, accNo)
            

                

























# def getBalance(name,amount):
#      file_path = "Bank-Management-System\\accounts.json"

#     # Load existing accounts
#      with open(file_path, "r") as file:
#         accounts = json.load(file)

#     # Update balance for the given user
#      for account in accounts:
#         if account["name"] == name:
#             account["balance"] += amount
#             break  # Stop loop after updating the correct user

#     # # Save updated data back to the file
#      with open(file_path, "w") as file:
#         json.dump(accounts, file, indent=4)

        
        
# print(getBalance("haroon",6000))

        


               




        