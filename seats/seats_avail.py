import sqlite3
conn=sqlite3.connect( "theatre_db.db" )


def check_seats(mid):
    s = conn.execute( "select seat_list from theatre where mid='" + str( mid ) + "'" )
    for i in s:
        s_list = i[0]
   # print(s_list)
    str_list = s_list.split()
   # print(str_list)

    for i in range( len( str_list ) ):
        str_list[i] = int(str_list[i])
    return str_list
