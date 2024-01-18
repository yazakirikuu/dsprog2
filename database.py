#ローカルデータ
import sqlite3

# DBファイル名
db_name = 'test.sqlite'

# DBに接続する（指定したDBファイル存在しない場合は，新規に作成される）
con = sqlite3.connect

# DBへの接続を閉じる
con.close()
# 1．DBに接続する
con = sqlite3.connect
# print(type(con))

# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()

sql_create_table_gdp = 'CREATE TABLE cars(id int, name text, gdp real);'

# 4．SQLを実行する
cur.execute(sql_create_table_gdp)


con.close()
# 1．DBに接続する
con = sqlite3.connect
# print(type(con))

# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 3．SQLを用意
# データを挿入するSQL
# INSERT INTO テーブル名 VALUES (列に対応したデータをカンマ区切りで);
sql_insert_many = "INSERT INTO gdp VALUES (?, ?, ?);"

# データをリストで用意する
cars_list = [
    (1, 'japan', 1500),
    (2, 'germany', 800),
    (3, 'NSX-R', 1200),
]

# 4．SQLを実行
cur.executemany(sql_insert_many, cars_list)

# 5．コミット処理（データ操作を反映させる）
con.commit()

# 6．DBへの接続を閉じる
con.close()