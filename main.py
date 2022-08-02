import sqlite3

conn = sqlite3.connect('db.sqlite3')
cur = conn.cursor()
# row = cur.execute('CREATE TABLE DRUG ("NAME" TEXT)');
row = cur.execute('SELECT * FROM basic_app_mymodel1').fetchall()
print(row)


