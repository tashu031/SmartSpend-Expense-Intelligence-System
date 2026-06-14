from database import get_connection


def budget_alert(user_id=None):
    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return
    if user_id is None:
        user_id = int(input("Enter your User Id: "))

    cursor = conn.cursor()
    try:
        budget = float(input("Enter Monthly Budget: "))
    except ValueError:
        print("Invalid budget!")
        cursor.close()
        conn.close()
        return
    if budget <= 0:
        print("Budget must be greater than 0!")
        conn.close()
        return
    
    sql = """
    select sum(amount) as total_expense from expense where user_id = ? 
    """

    cursor.execute(sql, (user_id,))

    total_expense = cursor.fetchone()[0]
    if total_expense is None:
        total_expense = 0

    if total_expense < budget:
        remaining = budget - total_expense
    else:
        excess = total_expense - budget

    print("\n===== BUDGET REPORT  =====")
    print(f"Budget         : ₹{budget}")
    print(f"Total Expense  : ₹{total_expense}")

    if total_expense > budget:
        print(f"⚠ Budget Exceeded by ₹{excess}")
    else:
        print(f"✅ Within Budget\nRemaining Budget : ₹{remaining}")

    cursor.close()
    conn.close()


