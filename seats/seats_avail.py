import sqlite3
conn=sqlite3.connect( "theatre_db.db" )
from admin import insert_mv as im


def check_seats(mid):
    s = conn.execute( "select seat_list from theatre where mid='" + str( mid ) + "'" )
    for i in s:
        slist = i[0]
    str_list = slist.split()
    print( str_list )
    for i in range( len( str_list ) ):
        str_list[i] = int( str_list[i] )
    return str_list
