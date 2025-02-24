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


# import json
import json
import os

class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def setName(self, name):
        self.name = name

    def getBalance(self):
        return self.balance  # Corrected to return only balance

    def toDict(self):
        return {"name": self.name, "balance": self.balance}

    def saveAcc(self):
        file_path = "Bank-Management-System\\accounts.json"

        # Check if file exists and load existing data
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:  # Ensure file isn't empty
            with open(file_path, "r") as file:
                try:
                    accounts = json.load(file)
                    if not isinstance(accounts, list):  # Ensure it's a list
                        accounts = []
                except json.JSONDecodeError:
                    accounts = []  # Handle corrupted/empty JSON file
        else:
            accounts = []

        # Append new account data
        accounts.append(self.toDict())

        # Save updated list back to file
        with open(file_path, "w") as file:
            json.dump(accounts, file, indent=4)

    @staticmethod
    def getBalanceByName(name):
        file_path = "Bank-Management-System\\accounts.json"

        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            with open(file_path, "r") as file:
                try:
                    accounts = json.load(file)
                except json.JSONDecodeError:
                    return None  # If file is empty or corrupted

            # Search for the account by name
            for acc in accounts:
                if acc.get("name") == name:
                    return acc.get("balance")

        return None  # Account not found

# Example Usage
acc1 = Bank("Haroon", 5000)
acc1.saveAcc()

acc2 = Bank("Ali", 7000)
acc2.saveAcc()

# Get balance by name
print(Bank.getBalanceByName("Haroon"))  # Output: 5000
print(Bank.getBalanceByName("Ali"))     # Output: 7000
print(Bank.getBalanceByName("Unknown")) # Output: None

        


               

# dic = {"AccountNumber":343434,"Name":"Haroon Abbas","Balance":0}

# with open("Bank-Management-System\\accounts.json", "w") as file:
#     json.dump(dic, file, indent=4)  # Makes the JSON file more readable

    
    


        