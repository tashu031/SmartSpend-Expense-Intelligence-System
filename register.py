from database import get_connection

def register_user():

    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return

    cursor = conn.cursor()

    name = input("Enter Your Name: ")
    email = input("Email: ")
    password = input("Password: ")

    sql = """
    INSERT INTO users(name, email, password)
    VALUES (?, ?, ?)
    """

    cursor.execute(sql, (name, email, password))

    conn.commit()

    print("User registered successfully!")

    cursor.close()
    conn.close()