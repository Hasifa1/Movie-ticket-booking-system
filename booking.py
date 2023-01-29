import sqlite3
conn=sqlite3.connect("moviedb.db")
from user_interface import seats
#seats=[]
def book_ticket(c_name,t_name,movie_name,seat_no):

    if seat_no in seats:
        print('this seat is already booked go for another seat:')
    else:
        c_data = {}
        c_data['c_name'] = c_name
        c_data['t_name'] = t_name
        c_data['movie_name'] = movie_name
        c_data['seat_no'] = seat_no
        seats.append(seat_no)
        conn.execute('''
                insert into booking_details(c_name,t_name,movie_name,seat_no) values(?,?,?,?)
            ''', (c_data.get("t_id"), c_data.get("t_name"), c_data.get("movie_name"), c_data.get("seat_no")))
        print('ur ticket is successfully booked')
    return seats
