from database import get_connection
def add_income():
    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return

    cursor = conn.cursor()

    user_id = int(input("Enter your User Id :"))
    income = int( input("Income :"))
    source = input("Source of Income :")
    date = input("Date (YYYY-MM-DD):")

    sql = """
    insert into income (user_id, amount , source, income_date)
    values (?,?,?,?)
    """

    cursor.execute(sql , (user_id, income,source,date))
    conn.commit()

    print("Income added successfully!")
    cursor.close()
    conn.close()