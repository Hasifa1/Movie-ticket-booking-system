import sqlite3
conn=sqlite3.connect("theatre_db.db")
from MainApp import insert_mv as im
def book_ticket(c_id, m_no, m_name, seat_num, mid):

    c_data = {}
    c_data['c_id'] = c_id
    c_data['m_no'] = m_no
    c_data['m_name'] = m_name
    c_data['seat_num'] = seat_num

    im.seats_dict[mid].remove(seat_num)
    conn.execute( '''
                insert into book_det(c_id,m_no,m_name,seat_num) values(?,?,?,?)
            ''', (c_data.get( "c_id" ), c_data.get( "m_no" ), c_data.get( "m_name" ), c_data.get( "seat_num" )) )
    print('ur ticket is successfully booked')
