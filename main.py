from register import register_user
from login import login_user
from income import add_income, update_income, delete_income
from expense import add_expense, update_expense, delete_expense
from view_expense import view_expenses
from monthly_summary import monthly_summary
from expense_analysis import expense_analysis
from view_income import view_incomes
from top_spending_category import view_top_spend
from budget_alert import budget_alert

def main_menu():
    current_user = None
    current_user_id = None

    while True:
        print("\n===== SMARTSPEND =====")

        if current_user:
            print(f"Logged in as: {current_user['name']} (User ID: {current_user_id})")
        else:
            print("Not logged in. Please register or login.")

        print("1. Register")
        print("2. Login")
        print("3. Logout")
        print("4. Add Income")
        print("5. Update Income")
        print("6. Delete Income")
        print("7. Add Expense")
        print("8. Update Expense")
        print("9. Delete Expense")
        print("10. View Expenses")
        print("11. View Income")
        print("12. Monthly Summary")
        print("13. Expense Analysis")
        print("14. View Top Spending Category")
        print("15. Budget Alert")
        print("16. Exit\n")

        try:
            choice = int(input("Select your Choice: "))
        except ValueError:
            print("Please enter a valid choice!")
            continue

        if choice in range(4, 16) and current_user_id is None:
            print("Please login first to use this feature.")
            continue

        match choice:
            case 1:
                register_user()

            case 2:
                user = login_user()
                if user:
                    current_user = user
                    current_user_id = user["user_id"]

            case 3:
                if current_user:
                    print(f"User {current_user['name']} logged out.")
                    current_user = None
                    current_user_id = None
                else:
                    print("No user is currently logged in.")

            case 4:
                add_income(current_user_id)

            case 5:
                update_income(current_user_id)

            case 6:
                delete_income(current_user_id)

            case 7:
                add_expense(current_user_id)

            case 8:
                update_expense(current_user_id)

            case 9:
                delete_expense(current_user_id)

            case 10:
                view_expenses(current_user_id)

            case 11:
                view_incomes(current_user_id)

            case 12:
                monthly_summary(current_user_id)

            case 13:
                expense_analysis(current_user_id)

            case 14:
                view_top_spend(current_user_id)

            case 15:
                budget_alert(current_user_id)

            case 16:
                confirm = input("Are you sure you want to exit? (y/n): ").strip().lower()
                if confirm == "y":
                    print("Thank you for using SmartSpend!")
                    break

            case _:
                print("Invalid Choice!")


if __name__ == "__main__":
    main_menu()
