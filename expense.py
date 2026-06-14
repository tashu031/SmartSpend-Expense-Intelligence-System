from database import get_connection

def add_expense(user_id=None):
    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return

    if user_id is None:
        user_id = int(input("Enter your User Id: "))

    cursor = conn.cursor()

    
    try:
        amount = float(input("Amount: "))
    except ValueError:
        print("Invalid Amount!")
        cursor.close()
        conn.close()
        return
    
    if amount <= 0:
        print("Expense amount must be greater than 0!")
        cursor.close()
        conn.close()
        return
    
    category = input("Category: ")
    if not category.strip():
        print("Category cannot be empty!")
        cursor.close()
        conn.close()
        return

    description = input("Description: ")
    date = input("Expense Date (YYYY-MM-DD): ")


    sql = """
    insert into expense (user_id,amount,category,description,expense_date)
    values (?,?,?,?,?)
    """
    cursor.execute(sql, (user_id, amount, category, description, date))
    conn.commit()

    print("Expense added successfully!")
    cursor.close()
    conn.close()