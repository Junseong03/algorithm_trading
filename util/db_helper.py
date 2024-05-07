import sqlite3
# conn = sqlite3.connect("universe_price.db", isolation_level=None)
# cur = conn.cursor()

with sqlite3.connect('universe_price.db') as conn:
    cur = conn. cursor()

sql = "delete from balance where will_clear_at=:will_clear_at"
cur.execute(sql, {"will_clear_at": "next"})

print(cur.rowcount)
conn.commit()