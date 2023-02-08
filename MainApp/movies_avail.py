import sqlite3
conn=sqlite3.connect("theatre_db.db")
def get_data():
    r=conn.execute('select count(*) from theatre')
    for i in r:
        no=int(i[0])
    if no==0:
        print('no movies are running now')
    else:
        records = conn.execute('select * from theatre')
        for i in records:
            print(i)