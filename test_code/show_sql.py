import sqlite3
c = sqlite3.connect("database.db")

sql = "SELECT * FROM acc_data, item"
s = c.cursor()
s.execute(sql)

for row in s:
    print(row)

c.close()