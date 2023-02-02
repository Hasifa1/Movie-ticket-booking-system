from MainApp import insert_mv as i
from MainApp import movies_avail as m_a
from MainApp import seats_avail as s
from MainApp import bookings as b
from MainApp import view_bookings as vb
while True:
    print('''
    1.owner login .
    2.Fetch the details of movies 
    3.Book the tickets
    4.view the bookings
    5.exit from app
    ''')
    print("choose any option from the above")
    ch = int(input())
    if ch == 1:
        # print('enter ur userid and pwd')
        userid='1001'
        p='1234'
        u_id=input('enter user id')
        pwd=input('enter ur pwd')
        if u_id == userid and pwd == p:
            print('valid login')
            i.input_data()
        else:
            print("login invalid")
    elif ch == 2:
        print('Movies available in this theatre')
        m_a.get_data()
    elif ch == 3:
        print('give details of the customer and book the ticket')
        c_id = input('enter ur id or name:')
        m_no = input('enter mobile number:')
        m_name = input('enter movie name:')
        mid=int(input('enter movie id:'))
        sl=s.check_seats(mid)
        print(sl)
        seat_num = int(input('enter seat no:'))
        if seat_num in sl:
            b.book_ticket(c_id, m_no, m_name, seat_num,mid)
        else:
            print("this seat is already booked")
    elif ch == 4:
        print('view the bookings')
        vb.get_bookings()
    else:
        break
