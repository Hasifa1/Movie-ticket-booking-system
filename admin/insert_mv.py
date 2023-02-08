import sqlite3
conn = sqlite3.connect( "theatre_db.db" )
def input_data():
    mid = int(input("enter the movie id"))
    name = input("enter movie name")
    no_of_seats = int(input("enter no of seats"))
    data = {}
    data['mid'] = mid
    data['name'] = name
    data['no_of_seats'] = no_of_seats

    li=[]
    for i in range(1,no_of_seats+1):
        li.append(i)
    st=''
    for i in li:
        st=st+str(i)+' '
    #print(st)
    data['seat_list']=st
    conn.execute('''
        insert into theatre(mid,name,no_of_seats,seat_list) values(?,?,?,?)
    ''', (data.get("mid"), data.get("name"), data.get("no_of_seats"),data.get("seat_list")))

    conn.commit()

    print('data entered successfully')
def del_data():
    mid=int(input('enter the movie id of the movie u wanted to delete'))
    conn.execute("delete from theatre where mid='"+str(mid)+"'")
    conn.commit()
    print('successfully deleted')
