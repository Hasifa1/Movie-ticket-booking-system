import sqlite3
"moviedb.db"
conn=sqlite3.connect("moviedb.db")
query1='''
create table theatre(t_id int primary key,t_name text not null,movie_name text not null,no_seats int not null)
'''
query2='''
create table booking_details(c_name text not null,t_name text not null,movie_name text not null,seat_no int not null)
'''
conn.execute(query1)