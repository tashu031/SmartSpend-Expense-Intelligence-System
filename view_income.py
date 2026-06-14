from database import get_connection

def view_incomes(user_id=None):
    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return

    if user_id is None:
        user_id = int(input("Enter your User Id: "))

    cursor = conn.cursor()

    sql = """
    select * from income where user_id = ?
    """
    cursor.execute(sql, (user_id,))
    user_incomes = cursor.fetchall()

    print("\n===== Income History =====\n")
    if not user_incomes:
        print("No income records found.")
    else:
        for row in user_incomes:
            print(f"Income ID   : {row[0]}")
            print(f"Amount      : ₹{row[2]}")
            print(f"Source      : {row[3]}")
            print(f"Income Date : {row[4]}")
            print("-" * 30)
    cursor.close()
    conn.close()
