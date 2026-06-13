from database import get_connection
def add_expense():
   
    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return
    cursor = conn.cursor()

    user_id = int(input("Enter your User Id :"))
    amount = int(input("Amount :"))
    category = input("Category :")
    description = input("Description :")
    date = input("Expense Date (YYYY-MM-DD) :")

    sql = """
    insert into expense (user_id,amount,category,description,expense_date)
    values (?,?,?,?,?)
    """
    cursor.execute(sql,(user_id,amount,category,description,date))
    conn.commit()

    print("Expense added successfully!")
    cursor.close()
    conn.close()