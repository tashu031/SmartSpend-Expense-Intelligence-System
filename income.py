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