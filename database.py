import sqlite3

# DBファイル名
db_name = 'test.sqlite'

# 1．DBに接続する
con = sqlite3.connect(db_name)  # You need to call the connect method with the database name

# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 3．テーブルを作成するSQL
sql_create_table_gdp = 'CREATE TABLE gdp(id int, name text, gdp real);'

# 4．SQLを実行する
cur.execute(sql_create_table_gdp)

# 1．DBに接続する（新しい接続を作成する）
con = sqlite3.connect(db_name)

# 2．SQLを実行するためのオブジェクトを取得
cur = con.cursor()

# 3．データを挿入するSQL
sql_insert_many = "INSERT INTO gdp VALUES (?, ?, ?);"

# 4．データをリストで用意する
cars_list = [
    (1, 'japan', 3931266),
    (2, 'india', 225659),
    (3, 'germany', 5120355),
    (4, 'France', 4365898),
    (5, 'Iran', 409121),
    (6, 'Iceland', 6872764),
]

# 5．SQLを実行
cur.executemany(sql_insert_many, cars_list)

# 6．コミット処理（データ操作を反映させる）
con.commit()

# 7．DBへの接続を閉じる
con.close()
