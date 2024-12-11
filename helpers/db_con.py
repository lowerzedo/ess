import cx_Oracle
from helpers.secret import get_secret


def execute_update(fn):
    def wrapper(query_obj):
        oracle_db = get_secret()[0].split(':')
        dsn_tns = cx_Oracle.makedsn(oracle_db[0], oracle_db[1], oracle_db[2])
        conn = cx_Oracle.connect(oracle_db[3], oracle_db[4], dsn=dsn_tns, encoding="UTF-8", nencoding="UTF-8")
        cursor = conn.cursor()
        query = fn(query_obj)
        cursor.execute(query, query_obj)
        conn.commit()
        cursor.close()
        conn.close()
        return True 
    return wrapper