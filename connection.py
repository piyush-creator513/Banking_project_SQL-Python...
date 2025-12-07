
import pyodbc

def get_connection():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=.;'
            'DATABASE=bank530;'
            'Trusted_Connection=yes;'
        )
        print("✅ Database connection successful!")
        return conn  # ✅ Return the connection here (important)

    except Exception as e:
        print("❌ Database connection failed:", e)
        return None
