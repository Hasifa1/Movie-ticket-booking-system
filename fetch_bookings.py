import sqlite3
conn = sqlite3.connect("moviedb.db")
def get_bookings():
    records = conn.execute('select * from booking_details')
    print(records)
    for i in records:
        print(i)
