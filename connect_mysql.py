import mysql.connector as msc

conn = msc.connect(
    host='localhost',
    user='kakeibo',
    password='hibiki',
    database='kakeibo'
)

print(conn.is_connected())

cur = conn.cursor()
cur.execute("SELECT * FROM acc_data, item")
rows = cur.fetchall()
for row in rows:
    print(row)
