import sqlite3

conn = sqlite3.connect("moviedb.db")
# from user_interface import seats


def input_data():
    t_id = int(input("enter the theatre id"))
    t_name = input("enter theatre name")
    movie_name = input("enter movie name")
    no_seats = int(input("enter no of seats"))
    data = {}
    data['t_id'] = t_id
    data['t_name'] = t_name
    data['movie_name'] = movie_name
    data['no_seats'] = no_seats
    # for i in range(no_seats):
    #   seats.append['1']
    conn.execute('''
        insert into participants(t_id,t_name,movie_name,no_seats) values(?,?,?,?)
    ''', (data.get("t_id"), data.get("t_name"), data.get("movie_name"), data.get("no_seats")))

    conn.commit()
    print('data entered successfully')
    return data
