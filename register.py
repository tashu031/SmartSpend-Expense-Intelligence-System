import pyodbc
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=smart_spend ;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

name = input("enter your name : ")
email = input("email :")
password = input("password :")

sql = """
insert into users(name,email,password)
values(?,?,?)

"""
cursor.execute(sql,(name,email,password))
conn.commit()

print("User registered successfully")

cursor.close()
conn.close()
