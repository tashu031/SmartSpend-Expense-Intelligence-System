from database import get_connection

def register_user():

    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return

    cursor = conn.cursor()

    name = input("Enter Your Name: ").strip()
    email = input("Email: ").strip().lower()
    password = input("Password: ")

# Empty field validation
    if not name:
        print("Name cannot be empty!")
        cursor.close()
        conn.close()
        return

    if not email:
        print("Email cannot be empty!")
        cursor.close()
        conn.close()
        return

    if not password:
        print("Password cannot be empty!")
        cursor.close()
        conn.close()
        return

# Email format validation
    if "@" not in email or "." not in email:
        print("Invalid email format!")
        cursor.close()
        conn.close()
        return

# Password validation
    if len(password) < 6:
        print("Password must be at least 6 characters!")
        cursor.close()
        conn.close()
        return

# Duplicate email check
    cursor.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    )

    existing_user = cursor.fetchone()

    if existing_user:
        print("Email already registered!")
        cursor.close()
        conn.close()
        return

# insert new user
    sql = """
    INSERT INTO users(name, email, password)
    VALUES (?, ?, ?)
    """

    cursor.execute(sql, (name, email, password))
    conn.commit()

    print("User registered successfully!")

    cursor.close()
    conn.close()