import sqlite3
conn = sqlite3.connect("universe_price.db", isolation_level=None)

cur = conn.cursor()
# 드래그 하고 CTAL + /
# 입력기 변경 단축키 : CTAL + SHIFT
# cur.execute('''CREATE TABLE balance
#                 (
#                 code varchar(6) PRIMARY KEY,
#                 bid_price int(20) NOT NULL,
#                 quantity int(20) NOT NULL,
#                 created_at varchar(14) NOT NULL,
#                 will_clear_at varchar(14)
#                 )''')

sql = 'insert into balance(code, bid_price, quantity, created_at, will_clear_at) values(?,?,?,?,?)'
cur.execute(sql,('000600', 173200, 10, '20240507', 'today'))

print(cur.rowcount)


conn.commit()