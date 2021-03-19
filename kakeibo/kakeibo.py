
import sqlite3

# 空のデータベースを作成して接続
dbname = "database.db"
c = sqlite3.connect(dbname)
# 外部キー制約オプションを有効にする
c.execute("PRAGMA foreign_keys = 1")

# itemテーブルの定義
ddl = """CREATE TABLE item(
    item_code INTEGER PRIMARY KEY,
    item_name TEXT NOT NULL UNIQUE
);
"""

# SQLの発行
c.execute(ddl)

# acc_dataテーブルの定義
ddl = """CREATE TABLE acc_data(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    acc_data DATA NOT NULL,
    item_code INTEGER NOT NULL,
    amount INTEGER,
    FOREIGN KEY(item_code) REFERENCES item(item_code)
);
"""

# SQLの発行
c.execute(ddl)

# itemテーブル登録のテスト
c.execute("INSERT INTO item VALUES(1,'食費');")
c.execute("INSERT INTO item VALUES(2,'住宅費');")
c.execute("INSERT INTO item VALUES(3,'光熱費');")
c.execute("COMMIT;")

# acc_dataテーブル登録テスト
c.execute(
    """INSERT INTO acc_data(acc_data,item_code,amount)
    VALUES('2021-3-15',1,1000);
    """
)
c.execute("COMMIT;")

# acc_dataテーブル登録テスト（変数を使った登録）
data = "'{}-{}-{}'".format(2021,3,15)
code = 2
amount = 2000

c.execute(
    """INSERT INTO acc_data(acc_data,item_code,amount)
    VALUES({},{},{});""".format(data,code,amount)
)
c.execute("COMMIT;")

# 最後に登録されているデータの表示して確認する。
# itemテーブルの表示
result = c.execute("SELECT * FROM item;")
for row in result:
    print(row)

# acc_dataテーブルの表示
result = c.execute("SELECT * FROM acc_data;")
for row in result:
    print(row)

# acc_dataテーブルとitemテーブルを結合して表示する
result = c.execute(
    """SELECT a.acc_data, i.item_name, a.amount
    FROM acc_data as a,item as i
    WHERE a.item_code = i.item_code;"""
)
for row in result:
    print(row)
