from database import get_connection

def monthly_summary(user_id=None):
    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return

    if user_id is None:
        user_id = int(input("Enter your User Id: "))

    cursor = conn.cursor()

    cursor.execute(""" select sum(amount) from income where user_id = ?
    """ , (user_id,))
    total_income = cursor.fetchone()[0]

    cursor.execute(""" select sum(amount) from expense where user_id = ?
    """ , (user_id,))
    total_expenses = cursor.fetchone()[0]

    if total_income is None:
        total_income = 0
    if total_expenses is None:
        total_expenses = 0

    savings = total_income - total_expenses
    if total_income == 0:
        saving_percent = 0
    else:
        saving_percent = (savings / total_income) * 100

    print("\n===== Monthly Summary =====")
    print(f"User Id       : {user_id}")
    print(f"Total Income  : ₹{total_income}")
    print(f"Total Expense : ₹{total_expenses}")
    print(f"Savings       : ₹{savings}")

    if saving_percent >= 30:
        status = "Excellent"
    elif saving_percent >= 15:
        status = "Good"
    else:
        status = "Needs Improvement"

    print(f"\nSavings Percentage : {saving_percent:.2f} %")
    print(f"Status : {status}")

    cursor.close()
    conn.close()

