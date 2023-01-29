from MainApp import insert_into_theatre as i
from MainApp import fetch_data as f
from MainApp import booking as b
from MainApp import fetch_bookings as fb
seats=[]
while True:
    print('''
    1.enter details of the movie.
    2.Fetch the details of movies 
    3.Book the tickets
    4.view the bookings
    5.exit from app
    ''')
    print("choose any option from the above")
    ch = int(input())
    if ch == 1:
        print('enter the movie details in the data base')
        i.input_data()
    elif ch == 2:
        print('to fetch the database')
        f.get_data()
    elif ch == 3:
        print('give details of the customer and book the ticket')
        c_name = input('enter ur name:')
        t_name = input('enter theatre name:')
        movie_name = input('enter movie name:')
        seat_no = int(input('enter seat no:'))
        b.book_ticket(c_name, t_name, movie_name, seat_no)
    elif ch == 4:
        print('view the bookings')
        fb.get_bookings()
    else:
        break
