import sqlite3

def check_table_exist(db_name, table_name):
    with sqlite3.connect('universe_price.db') as con:
        cur = con.cursor()
        sql = "SELECT name FROM sqlite_master WHERE type='table' and name=:table_name"
        cur.execute(sql, {"table_name": table_name})

    if len(cur.fetchall()) > 0:
        return True

    else:
        return False
