from database import get_connection

def login_user():
    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return None

    cursor = conn.cursor()

    email = input("Enter Your Email: ").strip().lower()
    password = input("Password: ")

    
    if not email.strip():
        print("Email cannot be empty!")
        cursor.close()
        conn.close()
        return

    if not password.strip():
        print("Password cannot be empty!")
        cursor.close()
        conn.close()
        return

    sql = """
    select * from users where email=? and password=?
    """
    cursor.execute(sql, (email, password))

    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user:
        print("Login successful!")
        return {"user_id": user[0], "name": user[1], "email": user[2]}

    print("❌ Invalid Credentials!")
    return None
