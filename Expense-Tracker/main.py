import pandas as pd
from datetime import datetime
class ExpenseTracker:
    def __init__(self,fileName="Expense-Tracker\\expense.csv"):
        self.fileName=fileName
        self.df=self.loadExpense()
    def loadExpense(self):
        try:
            df=pd.read_csv(self.fileName,parse_dates=['Date'])
        except:
            df=pd.DataFrame(columns=["Date","Category","Amount","Notes"])
        return df
    def saveExpense(self):
        self.df.to_csv(self.fileName,index=False)

    def addExpense(self):
        date_str=input("Date[YYYY-MM-DD] [Leave Blank For Today]")
        if date_str.strip()=='':
            date=pd.Timestamp.today().normalize()
        else:
            date=pd.to_datetime(date_str).normalize()
        category=input("Enter the Category : ")
        amount=float(input("Enter the amount :"))
        notes=input("Add Notes")
        newExpense=pd.DataFrame([
            {
                "Date":date,
                "Category":category,
                "Amount":amount,
                "Notes":notes
            }
        ])
        self.df=pd.concat([self.df,newExpense],ignore_index=True)
        self.saveExpense()
        print("Expense Added")
    def veiwExpenses(self,df=None):
        if df is None:
            df=self.df
        if df.empty:
            print("No Expense Found")
        else:
            print(df.to_string(index=False))


et=ExpenseTracker()
et.addExpense()
et.veiwExpenses()



