import sqlite3
conn=sqlite3.connect( "theatre_db.db" )


def book_ticket(c_id, m_no, m_name, seat_num, mid):

    c_data = {}
    c_data['c_id'] = c_id
    c_data['m_no'] = m_no
    c_data['m_name'] = m_name
    c_data['seat_num'] = seat_num

    s = conn.execute( "select seat_list from theatre where mid='" + str( mid ) + "'" )
    for i in s:
        slist=i[0]
    str_list=slist.split( )
    for i in range(len(str_list)):
        str_list[i]=int(str_list[i])
    str_list.remove(seat_num)
    st=''
    for i in str_list:
        st = st + str( i ) + ' '
    up_list=st
    conn.execute('''
    insert into book_det(c_id,m_no,c_name,seat_num) values(?,?,?,?)
    ''', (c_data.get( "c_id" ), c_data.get( "m_no" ), c_data.get( "m_name" ), c_data.get( "seat_num" )))
    conn.execute("update theatre set seat_list='"+up_list+"' where mid='"+str(mid)+"'")
    conn.commit()
    print('ur ticket is successfully booked')
