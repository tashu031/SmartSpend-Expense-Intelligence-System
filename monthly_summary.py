from database import get_connection
def monthly_summary():
    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return
    cursor = conn.cursor()

    user_id = int(input("Enter your User Id :"))

    cursor.execute(""" select sum(amount) from income where user_id = ?
    """ , (user_id,))
    total_income = cursor.fetchone()[0]

    cursor.execute(""" select sum(amount) from expense where user_id = ?
    """ , (user_id,))
    total_expenses = cursor.fetchone()[0]

    if total_income == None:
        total_income =0
    if total_expenses == None:
        total_expenses =0

    savings = total_income - total_expenses

    print("\n===== Montly Summery =====")

    print(f"User Id       : {user_id}")
    print(f"Total Income  : ₹{total_income}")
    print(f"Total Expense : ₹{total_expenses}")
    print(f"Savings       : ₹{savings}")
            
    cursor.close()
    conn.close()

