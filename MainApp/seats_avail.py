import sqlite3
conn=sqlite3.connect("theatre_db.db")
from MainApp import insert_mv as im
def check_seats(mid):

    return im.seats_dict.get(mid)
