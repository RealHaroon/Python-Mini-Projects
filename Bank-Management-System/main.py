class BankAccount:
    def __init__(self,acc_No,name,balance):
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



        