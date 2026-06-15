from database import get_connection

def add_income(user_id=None):
    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return

    if user_id is None:
        user_id = int(input("Enter your User Id: "))

    cursor = conn.cursor()

    try:
        income = float(input("Income: "))
    except ValueError:
        print("Invalid income amount!")
        cursor.close()
        conn.close()
        return
    

    if income <= 0:
        print("Income must be greater than 0!")
        cursor.close()
        conn.close()
        return
    
    source = input("Source of Income: ")
    if not source.strip():
        print("Source cannot be empty!")
        cursor.close()
        conn.close()
        return

    
    date = input("Date (YYYY-MM-DD): ")

    sql = """
    insert into income (user_id, amount , source, income_date)
    values (?,?,?,?)
    """

    cursor.execute(sql, (user_id, income, source, date))
    conn.commit()

    print("Income added successfully!")
    cursor.close()
    conn.close()


def update_income(user_id=None):
    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return

    if user_id is None:
        user_id = int(input("Enter your User Id: "))

    cursor = conn.cursor()
    sql = """
    select income_id, amount, source, income_date from income where user_id = ?
    """
    cursor.execute(sql, (user_id,))
    records = cursor.fetchall()

    if not records:
        print("No income records found.")
        cursor.close()
        conn.close()
        return

    print("\nYour income records:")
    for row in records:
        print(f"ID: {row[0]}, Amount: ₹{row[1]}, Source: {row[2]}, Date: {row[3]}")

    try:
        record_id = int(input("Enter Income ID to update: "))
    except ValueError:
        print("Invalid Income ID.")
        cursor.close()
        conn.close()
        return

    cursor.execute("select income_id from income where income_id = ? and user_id = ?", (record_id, user_id))
    if cursor.fetchone() is None:
        print("Income record not found.")
        cursor.close()
        conn.close()
        return

    try:
        new_amount = float(input("New income amount: "))
        if new_amount <= 0:
            raise ValueError
    except ValueError:
        print("Income amount must be a positive number.")
        cursor.close()
        conn.close()
        return

    new_source = input("New source of income: ").strip()
    if not new_source:
        print("Source cannot be empty!")
        cursor.close()
        conn.close()
        return

    new_date = input("New date (YYYY-MM-DD): ")
    update_sql = """
    update income set amount = ?, source = ?, income_date = ? where income_id = ? and user_id = ?
    """
    cursor.execute(update_sql, (new_amount, new_source, new_date, record_id, user_id))
    conn.commit()

    print("Income record updated successfully.")
    cursor.close()
    conn.close()


def delete_income(user_id=None):
    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return

    if user_id is None:
        user_id = int(input("Enter your User Id: "))

    cursor = conn.cursor()
    sql = """
    select income_id, amount, source, income_date from income where user_id = ?
    """
    cursor.execute(sql, (user_id,))
    records = cursor.fetchall()

    if not records:
        print("No income records found.")
        cursor.close()
        conn.close()
        return

    print("\nYour income records:")
    for row in records:
        print(f"ID: {row[0]}, Amount: ₹{row[1]}, Source: {row[2]}, Date: {row[3]}")

    try:
        record_id = int(input("Enter Income ID to delete: "))
    except ValueError:
        print("Invalid Income ID.")
        cursor.close()
        conn.close()
        return

    cursor.execute("select income_id from income where income_id = ? and user_id = ?", (record_id, user_id))
    if cursor.fetchone() is None:
        print("Income record not found.")
        cursor.close()
        conn.close()
        return

    confirm = input("Are you sure you want to delete this income record? (y/n): ").strip().lower()
    if confirm != "y":
        print("Delete cancelled.")
        cursor.close()
        conn.close()
        return

    cursor.execute("delete from income where income_id = ? and user_id = ?", (record_id, user_id))
    conn.commit()
    print("Income record deleted successfully.")
    cursor.close()
    conn.close()