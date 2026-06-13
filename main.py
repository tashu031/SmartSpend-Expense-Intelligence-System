from register import register_user
from login import login_user
from income import add_income
from expense import add_expense
from view_expense import view_expenses
from monthly_summary import monthly_summary
from expense_analysis import expense_analysis

def main_menu():
    while True:
        print("\n===== SMARTSPEND =====")
        print("1. Register")
        print("2. Login")
        print("3. Add Income")
        print("4. Add Expense")
        print("5. View Expenses")
        print("6. Monthly Summary")
        print("7. Expense Analysis")
        print("8. Exit \n")

        try:
            choice = int(input("Select your Choice: "))
        except ValueError :
            print("Please enter a Valid Choice !")
            continue
        match choice:
            case 1:
                register_user()

            case 2:
                login_user()

            case 3:
                add_income()

            case 4:
                add_expense()

            case 5:
                view_expenses()

            case 6:
                monthly_summary()

            case 7:
                expense_analysis()
            case 8:
                print("Thank you for using SmartSpend!")
                break
            case _:
                print("Invalid Choice!")


if __name__ == "__main__":
    main_menu()