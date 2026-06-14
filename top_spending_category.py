from database import get_connection

def view_top_spend(user_id=None):
    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return

    if user_id is None:
        user_id = int(input("Enter your User Id: "))

    cursor = conn.cursor()

    sql = """
    select top 1 category , sum(amount) as total from expense where user_id = ? group by category order by total desc
    """

    cursor.execute(sql, (user_id,))
    top_expense = cursor.fetchone()

    if top_expense:
        print("\n===== TOP SPENDING CATEGORY =====")
        print(f"Category : {top_expense[0]}")
        print(f"Total    : ₹{top_expense[1]}")
    else:
        print("No expense records found.")

    cursor.close()
    conn.close()