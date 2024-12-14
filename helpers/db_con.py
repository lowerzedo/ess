import pyodbc
from helpers.secret import get_secret


def execute_update(fn):
    def wrapper(query_obj):
        mssql_db = get_secret()[0].split(':')
        conn_str = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={mssql_db[0]},{mssql_db[1]};"
            f"DATABASE={mssql_db[2]};"
            f"UID={mssql_db[3]};"
            f"PWD={mssql_db[4]}"
        )
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        query = fn(query_obj)
        cursor.execute(query, query_obj)
        conn.commit()
        cursor.close()
        conn.close()
        return True 
    return wrapper