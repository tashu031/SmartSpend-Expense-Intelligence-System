from database import get_connection


def expense_analysis(user_id=None):
    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return

    if user_id is None:
        user_id = int(input("Enter your User Id: "))

    cursor = conn.cursor()
    sql = """
    select category , sum(amount) as expense from expense where user_id = ? group by category 
    """

    cursor.execute(sql, (user_id,))

    record = cursor.fetchall()

    print("\n===== Expense Analysis =====")
    if not record:
        print("No expense records found.")
    else:
        for row in record:
            print(f"Category : {row[0]}")
            print(f"Total    : ₹{row[1]}")
            print("-" * 25)
    cursor.close()
    conn.close()


