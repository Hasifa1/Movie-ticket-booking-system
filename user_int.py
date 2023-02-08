from admin import insert_mv as i
from MainApp import movies_avail as m_a
import bookings as b
from MainApp import view_bookings as vb
from seats import seats_avail as sa
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
        userid='Achievers'
        p='1234'
        u_id=input('enter user id')
        pwd=input('enter ur pwd')
        if u_id == userid and pwd == p:
            print('valid login')
            while True:
                print('1.insert movies')
                print('2.delete movies')
                print('3.exit from owner')
                print('choose any option')
                sc=int(input('enter ur option'))
                if sc==1:
                    i.input_data()
                elif sc==2:
                    i.del_data()
                else:
                    break
        else:
            print("login invalid")
    elif ch == 2:
        print('Movies available in this theatre:')
        m_a.get_data()
    elif ch == 3:
        c_id = input('enter ur id or name:')
        m_no = input('enter mobile number:')
        m_name = input('enter movie name:')
        mid=int(input('enter movie id:'))
        sl=[]
        sl.extend(sa.check_seats(mid))
        print('seats available are:\n')
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
