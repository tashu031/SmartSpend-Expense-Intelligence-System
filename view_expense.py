from database import get_connection

def view_expenses(user_id=None):
    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return

    if user_id is None:
        user_id = int(input("Enter your User Id: "))

    cursor = conn.cursor()

    sql = """
    select * from expense where user_id = ?
    """
    cursor.execute(sql, (user_id,))
    user_expenses = cursor.fetchall()

    if not user_expenses:
        print("No expense records found.")
    else:
        for row in user_expenses:
            print(
                f"Expense ID: {row[0]}, "
                f"Amount: ₹{row[2]}, "
                f"Category: {row[3]}, "
                f"Description: {row[4]}"
            )

    cursor.close()
    conn.close()
