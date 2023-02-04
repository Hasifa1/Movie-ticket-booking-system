import sqlite3
conn = sqlite3.connect("theatre_db.db")
def get_bookings():
    records = conn.execute("select * from book_det")
    for i in records:
        print(i)
