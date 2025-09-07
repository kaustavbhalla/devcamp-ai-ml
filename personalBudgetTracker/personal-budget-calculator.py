import shutil
import re
import csv

#Defining main function where maximum function take place :)
def main():
    print("Welcome to Personal Budget Calculator!".center(shutil.get_terminal_size().columns))

    name = input("name: ")
    print(f"Hello {name}")
    
    income, expenses = take_input()
    remainingMoney = saving(income,expenses)

    print(f"Your income: {income}\nYour expenses: {expenses}\nYour savings: {remainingMoney}")

    if remainingMoney < 0:
        print("You're in debt! You must decrease your expenses by filtering out all your unwanted purchases and being more responsible with money")
    elif remainingMoney <= 0.25 * income:
        print(f"You saved about {((remainingMoney/income)*100):.2f}% of your income, which falls within the 0-25 percent band of savings. Its good, but could be better!")
    elif remainingMoney <= 0.5 * income:
        print(f"You saved {((remainingMoney/income) * 100):.2f}% of your income, which falls within the 25-50% category of savings!")
    else:
        print(f"You saved {((remainingMoney/income) * 100):.2f}% of your income, great!")

    
    with open("BudgetTracker.csv",'a') as budgetFileoriginal:
        csvWriter = csv.writer(budgetFileoriginal)
        csvWriter.writerow([name,income,expenses,remainingMoney,(remainingMoney/income)*100])


#taking specific input and replacing words like k or l with their specific multipliers :)

def take_input():
    income = input("Enter your income in Rs.: ")
    expenses = input("Enter your expenses in Rs.: ")
    incomeCheckVal = income.replace(" ","").lower()
    expensesCheckVal = expenses.replace(" ","").lower()

    if "," in incomeCheckVal:
        income = int(income.replace(",", ""))
            

    elif "k" in incomeCheckVal:
        income = int(re.sub("k","",income,flags=re.IGNORECASE)) * 1000


    elif "l" in incomeCheckVal:
        income = int(re.sub("l","",income,flags=re.IGNORECASE)) * 100000



    if "," in expensesCheckVal:
        expenses = int(expenses.replace(",", ""))



    elif "k" in expensesCheckVal:
        expenses = int(re.sub("k","",expenses,flags=re.IGNORECASE)) * 1000

    elif "l" in expensesCheckVal:
        expenses = int(re.sub("l","",expenses,flags=re.IGNORECASE)) * 100000

    return income,expenses




#calculating saving
def saving(income,expenses):
    remMoney = income - expenses
    return remMoney


if __name__ == "__main__":
    main()

    
