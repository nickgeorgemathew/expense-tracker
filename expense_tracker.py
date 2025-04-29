import csv 
from datetime import datetime
import os
from collections import defaultdict
import matplotlib.pyplot as plt
FILENAME="expenses.csv"



if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Amount", "Category", "Description"])

def get_float_input(prompt):
    """Prompt user for a float input with validation."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❗ Please enter a valid number.")

def get_nonempty_string(prompt):
    """Prompt user for a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("❗ Input cannot be empty.")

def get_year_input(prompt):
    """Prompt user for a valid 4-digit year."""
    while True:
        try:
            year = int(input(prompt))
            if 1000 <= year <= 9999:
                return str(year)
            else:
                print("❗ Please enter a valid 4-digit year.")
        except ValueError:
            print("❗ Please enter numbers only.")






def addExpenses():
    amount = get_float_input("Enter the amount: ₹")
    category = get_nonempty_string("Enter the category for expenditure: ")
    description = get_nonempty_string("Enter description: ")
    date = datetime.now().strftime("%d/%m/%y,%H:%M:%S")

    with open(FILENAME,"a",newline='') as file:
        writer=csv.writer(file)
        writer.writerow([date,amount,category,description])
    print("category added")


def printExpenses():
    try:
        with open(FILENAME,'r') as file:
            reader= csv.reader(file)
            for row in reader:
                print(f"Date: {row[0]} | Amount: ₹{row[1]} | Category: {row[2]} | {row[3]}")
    except FileNotFoundError:
        print("No expenses found yet.")

def showTotal():
    total=0
    try:
        with open(FILENAME,'r') as file:
                reader= csv.reader(file)
                for row in reader:
                    total+=float(row[1])
        print(f"total is {total:%.2f}")
    except FileNotFoundError:
           print("No expenses or file found yet.")

def sortByCategory():
    try:
        with open(FILENAME,'r') as file:
                total=0
                reader= csv.reader(file)
                next(reader,None)
                expensebycategory_list=defaultdict(list)
                for row in reader:
                     if len(row)>=3:
                          date,amount,category,description=row
                          amount_float=float(amount)
                          expensebycategory_list[category].append(amount_float)
                for category in expensebycategory_list:
                     total={category:sum(expensebycategory_list[category] )for category in expensebycategory_list}
                     print("the total amount spent in ",category,"is",total[category])
        categories = list(expensebycategory_list.keys())
        totals = list(expensebycategory_list.values())

        plt.figure(figsize=(10,5))
        plt.bar(categories, totals, color='mediumseagreen', edgecolor='black')
        plt.xlabel("Category")
        plt.ylabel("Total Spend (₹)")
        plt.title("📊 Total Spend by Category")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()      
    except FileNotFoundError:
           print("No expenses or file found yet.")


def monthTotal():
    try:
        with open(FILENAME,'r') as file:
                total=0
                reader= csv.reader(file,skipinitialspace=True) 
                next(reader,None) 
                expensebymonth=defaultdict(list)          
                for row in reader:
                     
                     if len(row) >= 3:  
                          date,amount,category,description=row
                          month_obj=datetime.strptime(date,"%d/%m/%y,%H:%M:%S")
                          month=month_obj.strftime("%B %Y")
                          expensebymonth[month].append(float(amount))
                month_sorted=sorted(expensebymonth.keys(),key=lambda m:datetime.strptime(m,"%B %Y")) 
                totals={month:sum(expensebymonth[month]) for month in month_sorted}  
        
        for month in month_sorted:
             print(month,totals[month])                                        
                      
        plt.figure(figsize=(10,5))        
        plt.bar(month_sorted, [totals[month] for month in month_sorted])

        plt.xlabel(month)
        plt.ylabel("total spend")
        plt.xticks(rotation=45)
        plt.tight_layout()
        # plt.show()    

    except FileNotFoundError:
           print("No expenses or file found yet.")

def year_total() :
    try:

        with open(FILENAME,"r") as file:
             
             reader=csv.reader(file)
             next(reader,None)
             expensesbyyear=defaultdict(list)
             year_in=int(input("enter year"))
             for row in reader:
                  if len(row)>=3:
                    date,amount,category,description=row 
                    year_obj=datetime.strptime(date,"%d/%m/%y,%H:%M:%S")
                    year=year_obj.strftime("%Y")
                    expensesbyyear[year].append(float(amount))
                    year_sorted=sorted(expensesbyyear.keys(),key=lambda m:datetime.strptime(m,"%Y"))
                    total={year:sum(expensesbyyear[year]) for year in year_sorted}
                    

                    if year_in in expensesbyyear.items():
                     return(print(f"the total in {year_in:%.2f} is {total[year_in]:%.2f}"))
                     break
                         
                      
                    else:
                       return(print("year not present"))
                       break
        return             
                  


    except FileNotFoundError:
           print("No expenses or file found yet.")
         
         

          
     
 



def main():
    while True:
        print("\n📋 Expense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Spent by category")
        print("4. Monthly total")
        print("5. Yearly total")
        print("6. Exit")

        choice = input("Choose an option: ")
        if not use_match(choice):
            break  # Break loop if user chooses to exit

def use_match(choice):
    match choice:
        case "1":
            addExpenses()
            
        case "2":
            printExpenses()
           
        case "3":
            sortByCategory()
        case "4":
            monthTotal()
        case "5":
            year_total()
        case "6":
            print("👋 Exiting... Goodbye!")
            return False  # tell main loop to stop
        case _:
            print("Invalid choice. Try again.")
    return True  # keep going

                
            

if __name__=="__main__":
     main()
