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
        date_str=input("Date[YYYY-MM-DD] [Leave Blank For Today] :")
        if date_str.strip()=='':
            date=pd.Timestamp.today().normalize()
        else:
            date=pd.to_datetime(date_str).normalize()
        category=input("Enter the Category : ")
        amount=float(input("Enter the amount :"))
        notes=input("Add Notes : ")
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
    def filterByDate(self):
        startDate=input("Enter Start Date [YYYY,MM,DD] :")
        endDate=input("Enter End Date [YYYY,MM,DD] : ")
        startDate=pd.to_datetime(startDate)
        endDate=pd.to_datetime(endDate)
        filtered=self.df[(self.df['Date']>=startDate) &(self.df['Date']<=endDate)]
        self.veiwExpenses(filtered)
    def filterByCategory(self):
        cateGory=input("Enter Category :")
        filterd=self.df[self.df['Category']==cateGory]
        self.veiwExpenses(filterd)
    def veiwSummary(self):
        if self.df.empty:
            print("No Data !")
        total=self.df['Amount'].sum()
        avg=self.df['Amount'].mean()
        high=self.df['Amount'].max()
        print(f"Total Spent : {total}")
        print(f"Average Expense : {avg}")
        print(f"Highest Expense : {high}")
    def main(self):
        while True:
            print("Expense Tracker By Haroon 💵 💻")
            print("1. Add Expense ")
            print("2. View All Expense ")
            print("3. Filter by Date ")
            print("4. Filter by Category ")
            print("5. View Summary ")
            print("6. Exit")
            inp=input("Enter Your Choice (1-6) : ")
            if inp =="1":
                self.addExpense()
            elif inp=="2":
                self.veiwExpenses()
            elif inp=="3":
                self.filterByDate()
            elif inp=="4":
                self.filterByCategory()
            elif inp=="5":
                self.veiwSummary()
            elif inp=="6":
                print("Good Bye 👋 ")
                break
            else:
                print("Invalid Input!")
        


et=ExpenseTracker()
et.main()



