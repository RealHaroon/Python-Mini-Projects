from datetime import datetime

def ageCalculator():
    birth_year=int(input("Enter Your Birth year (YYYY):"))
    birth_month=int(input("Enter Your Birth month (MM): "))
    birth_day=int(input("Enter Your Birth Day (DD): "))

    #* get current date 
    today=datetime.today()
    birth_date=datetime(birth_year,birth_month,birth_day)
 
    #* Calculating Years,Months  and days
    years=today.year - birth_date.year
    months=today.month - birth_date.month
    days=today.day  - birth_date.day
    
    #* if birth month hasn't happened yet
    if months < 0:
        years -= 1
        months +=12 #* Convert negative month to positive

    #* If birth day hasn't happened yet
    if days < 0:
        months -=1
        last_month = (today.month - 1 ) if today.month > 1 else 12
        last_month_days = (datetime(today.year,last_month,1) - datetime(today.year , last_month - 1,1)).days
        days += last_month_days
    print(f"You are {years} Years , {months} Months and {days} Days Old.")

ageCalculator()