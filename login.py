from database import get_connection
def login_user():
   

    conn = get_connection()

    if conn is None:
        print("Database connection failed!")
        return

    cursor = conn.cursor()

    email = input("Enter Your Email :")
    password = input("Password :")

    sql ="""
    select * from users where email=? and password=?
    """
    cursor.execute(sql,(email,password))

    user = cursor.fetchone()
    if(user):
        print("Login sussessful ")
    else :
        print("Invalid Credentials !")

    cursor.close()
    conn.close()
