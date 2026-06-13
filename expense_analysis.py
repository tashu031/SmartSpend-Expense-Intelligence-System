from database import get_connection


def expense_analysis():
    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return
    cursor = conn.cursor()

    user_id = int(input("Enter your User Id :"))
    sql ="""
    select category , sum(amount) as expense from expense where user_id = ? group by category 
    """

    cursor.execute(sql,(user_id,))

    record = cursor.fetchall()

    print("\n===== Expense Analysis =====")
    for row in record:
        print(f"Category : {row[0]}")
        print(f"Total    : ₹{row[1]}")
        print("-" * 25)
    cursor.close()
    conn.close()


