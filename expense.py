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


def update_expense(user_id=None):
    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return

    if user_id is None:
        user_id = int(input("Enter your User Id: "))

    cursor = conn.cursor()
    sql = """
    select expense_id, amount, category, description, expense_date from expense where user_id = ?
    """
    cursor.execute(sql, (user_id,))
    records = cursor.fetchall()

    if not records:
        print("No expense records found.")
        cursor.close()
        conn.close()
        return

    print("\nYour expense records:")
    for row in records:
        print(f"ID: {row[0]}, Amount: ₹{row[1]}, Category: {row[2]}, Description: {row[3]}, Date: {row[4]}")

    try:
        record_id = int(input("Enter Expense ID to update: "))
    except ValueError:
        print("Invalid Expense ID.")
        cursor.close()
        conn.close()
        return

    cursor.execute("select expense_id from expense where expense_id = ? and user_id = ?", (record_id, user_id))
    if cursor.fetchone() is None:
        print("Expense record not found.")
        cursor.close()
        conn.close()
        return

    try:
        new_amount = float(input("New expense amount: "))
        if new_amount <= 0:
            raise ValueError
    except ValueError:
        print("Expense amount must be a positive number.")
        cursor.close()
        conn.close()
        return

    new_category = input("New category: ").strip()
    if not new_category:
        print("Category cannot be empty!")
        cursor.close()
        conn.close()
        return

    new_description = input("New description: ").strip()
    if not new_description:
        print("Description cannot be empty!")
        cursor.close()
        conn.close()
        return

    new_date = input("New expense date (YYYY-MM-DD): ")
    update_sql = """
    update expense set amount = ?, category = ?, description = ?, expense_date = ? where expense_id = ? and user_id = ?
    """
    cursor.execute(update_sql, (new_amount, new_category, new_description, new_date, record_id, user_id))
    conn.commit()

    print("Expense record updated successfully.")
    cursor.close()
    conn.close()


def delete_expense(user_id=None):
    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return

    if user_id is None:
        user_id = int(input("Enter your User Id: "))

    cursor = conn.cursor()
    sql = """
    select expense_id, amount, category, description, expense_date from expense where user_id = ?
    """
    cursor.execute(sql, (user_id,))
    records = cursor.fetchall()

    if not records:
        print("No expense records found.")
        cursor.close()
        conn.close()
        return

    print("\nYour expense records:")
    for row in records:
        print(f"ID: {row[0]}, Amount: ₹{row[1]}, Category: {row[2]}, Description: {row[3]}, Date: {row[4]}")

    try:
        record_id = int(input("Enter Expense ID to delete: "))
    except ValueError:
        print("Invalid Expense ID.")
        cursor.close()
        conn.close()
        return

    cursor.execute("select expense_id from expense where expense_id = ? and user_id = ?", (record_id, user_id))
    if cursor.fetchone() is None:
        print("Expense record not found.")
        cursor.close()
        conn.close()
        return

    confirm = input("Are you sure you want to delete this expense record? (y/n): ").strip().lower()
    if confirm != "y":
        print("Delete cancelled.")
        cursor.close()
        conn.close()
        return

    cursor.execute("delete from expense where expense_id = ? and user_id = ?", (record_id, user_id))
    conn.commit()
    print("Expense record deleted successfully.")
    cursor.close()
    conn.close()