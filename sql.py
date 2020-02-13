import sqlite3
import random
import datetime
import time

try:
    with sqlite3.connect("nrf.db") as conn:
        c = conn.cursor()
        sql = "CREATE TABLE if not exists Node_522274280  (Data integer, Date text, Time text, Last text )"
        c.execute(sql)
        conn.commit()

except sqlite3.OperationalError as error:
    print(error)


def test1():
    rr = 0.0
    with sqlite3.connect('nrf.db') as conn:
        while 1:
            rr += 10.0
            time_now = datetime.datetime.now()
            Date = time_now.strftime("%Y-%m-%d")
            Time = time_now.strftime("%H:%M:%S")
            if rr == 100:
                rr = 0
            print(rr)

            c = conn.cursor()
            # add star for last row
            sql = "INSERT INTO Node_522274280 (Data,Date,time,Last) values (?, ?, ?, ?)"
            c.execute(sql, (rr, Date, Time, ''))
            conn.commit()


###############################################################################
def test2():
    rr = 0.0
    while 1:
        with sqlite3.connect('nrf.db') as conn:
            rr += 10.0
            time_now = datetime.datetime.now()
            Date = time_now.strftime("%Y-%m-%d")
            Time = time_now.strftime("%H:%M:%S")
            c = conn.cursor()
            # add star for last row
            sql = "INSERT INTO Node_522274280 (Data,Date,time,Last) values (?, ?, ?, ?)"
            c.execute(sql, (rr, Date, Time, ''))
            conn.commit()
        # if rr == 100:
        #     rr = 0
        #time.sleep(1)
        print(rr)


#######################################################################
###################################################################################
def test3():
    rr = 0.0
    with sqlite3.connect('C:/Users/reza/Desktop/nrf_v1.1-98-9-18/LaserServer/nrf.db') as conn:
        while 1:
            for i in range(0, 1000):
                rr += 10.0
                time_now = datetime.datetime.now()
                Date = time_now.strftime("%Y-%m-%d")
                Time = time_now.strftime("%H:%M:%S")
                if rr == 100:
                    rr = 0
                print(rr)

                c = conn.cursor()
                # add star for last row
                sql = "INSERT INTO Laser_522274280 (Data,Date,time,Last) values (?, ?, ?, ?)"
                c.execute(sql, (rr, Date, Time, ''))
            conn.commit()


def Sq1_Fetch_Register():

    with sqlite3.connect("nrf.db") as conn:
        # mux data
        sql = "SELECT *  FROM  Node_522274280 where Data >'100' LIMIT 100 OFFSET 400"
        cursor = conn.execute(sql)
        data = cursor.fetchall()
        print(len(data))
        print(data)


# test2()
#Sq1_Fetch_Register()
test3()