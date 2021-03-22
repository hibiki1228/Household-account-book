import mysql.connector as msc


# DBに接続
conn = msc.connect(
    host='localhost',
    user='kakeibo',
    password='hibiki',
    database='kakeibo'
)
# 接続を確認
print(conn.is_connected())

cur = conn.cursor()

# itemテーブルの作成
cur.execute("DROP TABLE IF EXISTS 'item'")
cur.execute("""CREATE TABLE item(
    item_code INTEGER PRIMARY KEY,
    item_name TEXT NOT NULL UNIQUE
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci"""
)


# acc_dateテーブルの作成
cur.execute("DROP TABLE IF EXISTS acc_data")
cur.execute("""CREATE TABLE acc_data(
    id INT PRIMARY KEY AUTO_INCREMENT,
    acc_date DATE NOT NULL,
    item_code INT NOT NULL,
    amount INT,
    FOREIGN KEY(item_code) REFERENCES item(item_code))"""
)

# 仮データの入力
cur.execute("INSERT INTO item VALUES(1,'食費')")
cur.execute("INSERT INTO item VALUES(2,'住宅費')")
cur.execute("INSERT INTO item VALUES(3,'光熱費')")
cur.execute("COMMIT")

cur.execute(
    """INSERT INTO acc_data(acc_date,item_code,amount)
    VALUES('2021-3-15',1,1000);
    """
)
cur.execute("COMMIT;")


# 作成したデータの表示
cur.execute("SELECT * FROM acc_data, item")
rows = cur.fetchall()
for row in rows:
    print(row)
