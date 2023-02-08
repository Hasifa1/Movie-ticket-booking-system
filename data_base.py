import sqlite3
"theatre_db.db"
conn=sqlite3.connect("theatre_db.db")
query1=conn.execute('''
create table theatre(mid int primary key,name text not null,no_of_seats int default 500 not null,seat_list text)
''')
query2=conn.execute('''
create table book_det(c_id text primary key not null,m_no text not null,c_name text not null,seat_num int not null)
''' )
conn.commit()