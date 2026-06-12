import pyodbc

try:
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost\\SQLEXPRESS;"
        "DATABASE=smart_spend ;"
        "Trusted_Connection=yes;"
    )
    print("Database succesfully connected ...")

except Exception as e:
    print("Error :",e)