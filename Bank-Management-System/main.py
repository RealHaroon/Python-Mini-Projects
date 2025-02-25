import json
import os


class BankAccount:
    def __init__(self):
        self.filePath="Bank-Management-System\\accounts.json"
        self.loggenInAccount=None
    
    def login(self,name,accountNo):
        if os.path.exists(self.filePath) and os.path.getsize(self.filePath) > 0:
            with open(self.filePath, "r") as file:
                try:
                    accounts = json.load(file)
                except json.JSONDecodeError:
                    accounts = []  # If file is empty or corrupted
        else:
            accounts = []
    
        for account in accounts:
            if account["accountNo"] == accountNo and account["name"] == name:
                self.loggenInAccount=accountNo
                print("Login Succesful.")
                return True ,accountNo
        print("Invalid account Name or Number.")
        return False
    
    def deposit(self,amount):
        if self.loggenInAccount is None:
            print("Please login first.")
            return 
        with open(self.filePath,"r") as file:
            accounts=json.load(file)
        for account in accounts:
             if account==self.loggenInAccount :
                 account["balance"] += amount
                 print ( f"Deposited {amount}")
                 break
             
        with open(self.filePath,"w") as file:
            json.dump(accounts,file,indent=4)

    def withdraw(self,amount):
        if self.loggenInAccount is None:
            print("Please login first.")
            return 
        with open(self.filePath,"r") as file:
            accounts=json.load(file)
        for account in accounts:
             if account==self.loggenInAccount :
                 account["balance"] -= amount
                 print ( f"Withdrawn {amount}")
                 break
             
        with open(self.filePath,"w") as file:
            json.dump(accounts,file,indent=4)

    def getBalance(self):
        if self.loggenInAccount is None:
            print("Please login first.")
            return 
        with open(self.filePath,"r") as file:
            accounts=json.load(file)
        for account in accounts:
             if account==self.loggenInAccount :
                 print(f"Your current balance is : {account["balance"]}")
                 break
                


    
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
                print(f"Account with account number {accountNo} already exists")
        
        new_account={
                    "name":name,
                    "accountNo":accountNo,
                    "balance": 0

                }

        accounts.append(new_account)

        with open(self.filePath, "w") as file:
            json.dump(accounts, file, indent=4)
        print(  f"Account for {name} (Account No: {accountNo}) created successfully.")








            

                




















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

        


               




        