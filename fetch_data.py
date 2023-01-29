import sqlite3
conn=sqlite3.connect("moviedb.db")
def get_data():
    records = conn.execute('select * from theatre')
    print(records)
    for i in records:
        print(i)