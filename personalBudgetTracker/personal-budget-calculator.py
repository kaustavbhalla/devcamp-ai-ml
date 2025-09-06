import shutil
import re
import csv

def main():
    print("Welcome to Personal Budget Calculator!".center(shutil.get_terminal_size().columns))
    print("To get started, complete the fields below: ".center(shutil.get_terminal_size().columns))

    name = input("Enter your name to get started: ")
    print(f"Hello {name}, let's get you started on your expense tracking journey!")
    
    income, expenses = take_input()
    remainingMoney = calcRemMoney(income,expenses)

    print(f"Your income: {income}\nYour expenses: {expenses}\nYour savings: {remainingMoney}")

    if remainingMoney < 0:
        print("Damn! You're in debt! You must decrease your expenses by filtering out all your unwanted purchases and being more responsible with money")
    elif remainingMoney <= 0.25 * income:
        print(f"Good! You saved about {((remainingMoney/income)*100):.2f}% of your income, which falls within the 25 percent band of savings. Its good, but could be better!")
    elif remainingMoney <= 0.5 * income:
        print(f"Amazing! You saved {((remainingMoney/income) * 100):.2f}% of your income, which falls within the 25-50% category of savings!")
    else:
        print(f"Outstanding! You saved {((remainingMoney/income) * 100):.2f}% of your income, you're the GOAT!")

    with open("BudgetTracker.csv",'a') as budgetFile:
        cs = csv.writer(budgetFile)
        cs.writerow(["Name","Income","Expenses","Savings","Percent"])
    
    with open("BudgetTracker.csv",'a') as budgetFileoriginal:
        csvWriter = csv.writer(budgetFileoriginal)
        csvWriter.writerow([name,income,expenses,remainingMoney,(remainingMoney/income)*100])

def take_input():
    split_income_val = []
    split_expenses_val = []
    income = input("Enter your income in Rs.: ")
    expenses = input("Enter your expenses in Rs.: ")
    cr = "cr"

    if "," in income.replace(" ",""):
        split_income_val = income.split(",")
        income_substring = ""
        for i in split_income_val:
            income_substring += i

        income = int(income_substring)

    elif "k" in income.replace(" ","").lower():
        income = int(re.sub("k","",income,flags=re.IGNORECASE)) * 1000

    elif "l" in income.replace(" ","").lower():
        income = int(re.sub("l","",income,flags=re.IGNORECASE)) * 100000

    elif "cr" in income.replace(" ","").lower():
        income = int(re.sub("cr","",income,flags=re.IGNORECASE)) * 10000000


    if "," in expenses.replace(" ",""):
        split_expenses_val = expenses.split(",")
        expenses_substring = ""
        for i in split_expenses_val:
            expenses_substring += i

        expenses = int(expenses_substring)

    elif "k" in expenses.replace(" ","").lower():
        expenses = int(re.sub("k","",expenses,flags=re.IGNORECASE)) * 1000

    elif "l" in expenses.replace(" ","").lower():
        expenses = int(re.sub("l","",expenses,flags=re.IGNORECASE)) * 100000




    return income,expenses

    
def calcRemMoney(income,expenses):
    remMoney = income - expenses
    return remMoney


if __name__ == "__main__":
    main()

    
