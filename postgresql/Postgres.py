from Global import *
import psycopg2
import pymongo


#list Toutarial
#https://www.mongodb.com/download-center/enterprise
#https://stackabuse.com/working-with-postgresql-in-python/
#https://www.w3schools.com/python/python_json.asp
#https://www.postgresqltutorial.com/postgresql-python/call-stored-procedures/



user_postgres = "postgres"
password_postgres = "19972910"
host_postgres = "127.0.0.1"
port_postgres = "5432"
database_postgres = "IotKaran"


class PostgreSQL:


    def function (function_name, value_tuple=None):
        try:
            conn = psycopg2.connect(database=database_postgres, user=user_postgres, password=password_postgres, host=host_postgres, port=port_postgres)
            cur = conn.cursor()
            if value_tuple is None:
                cur.callproc(function_name)
            else:
                cur.callproc(function_name,value_tuple)

            aownser = cur.fetchall()
            print(aownser)

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)



    def select_Querry(querry, value_tuple=None):
        try:
            conn = psycopg2.connect(database=database_postgres, user=user_postgres, password=password_postgres, host=host_postgres, port=port_postgres)
            cur = conn.cursor()
            if value_tuple is None:
                cur.execute(querry)
            else:
                cur.execute(querry, value_tuple)

            rows = cur.fetchall()
            print(rows)
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)



    def Commit_Querry(querry, value_tuple=None):
        try:
            conn = psycopg2.connect(database=database_postgres, user=user_postgres, password=password_postgres,
                                    host=host_postgres, port=port_postgres)
            cur = conn.cursor()
            if value_tuple is None:
                cur.execute(querry)
            else:
                cur.execute(querry, value_tuple)

            cur.commit()
            cur.close()
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)



    def Creating_Table():

        con = psycopg2.connect(database=database_postgres, user=user_postgres, password=password_postgres, host=host_postgres, port=port_postgres)
        print("Database opened successfully")
        print(con)
        cur = con.cursor()
        cur.execute('''CREATE TABLE STUDENT
              (ADMISSION INT      NOT NULL,
              NAME           TEXT    NOT NULL,
              AGE            INT     NOT NULL,
              COURSE        CHAR(50),
              DEPARTMENT        CHAR(50));''')

        con.commit()
        con.close()

        print("Table created successfully")


    def Inserting_Data():
        con = psycopg2.connect(database=database_postgres, user=user_postgres, password=password_postgres, host=host_postgres, port=port_postgres)
        print("Database opened successfully")

        cur = con.cursor()

        cur.execute(
            "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')");

        con.commit()
        print("Record inserted successfully")
        con.close()


    def Retrieving_Data():

        con = psycopg2.connect(database=database_postgres, user=user_postgres, password=password_postgres, host=host_postgres, port=port_postgres)
        print("Database opened successfully")

        cur = con.cursor()
        cur.execute("SELECT admission, name, age, course, department from STUDENT")
        rows = cur.fetchall()

        for row in rows:
            print("ADMISSION =", row[0])
            print("NAME =", row[1])
            print("AGE =", row[2])
            print("COURSE =", row[3])
            print("DEPARTMENT =", row[4], "\n")

        print("Operation done successfully")
        con.close()



    def Updating_Tables():

        con = psycopg2.connect(database=database_postgres, user=user_postgres, password=password_postgres, host=host_postgres, port=port_postgres)
        print("Database opened successfully")

        cur = con.cursor()

        cur.execute("UPDATE STUDENT set AGE = 20 where ADMISSION = 3420")
        con.commit()
        print("Total updated rows:", cur.rowcount)

        cur.execute("SELECT admission, age, name, course, department from STUDENT")
        rows = cur.fetchall()
        for row in rows:
            print("ADMISSION =", row[0])
            print("NAME =", row[1])
            print("AGE =", row[2])
            print("COURSE =", row[2])
            print("DEPARTMENT =", row[3], "\n")

        print("Operation done successfully")
        con.close()


    def Deleting_Rows():
        con = psycopg2.connect(database=database_postgres, user=user_postgres, password=password_postgres, host=host_postgres, port=port_postgres)
        print("Database opened successfully")

        cur = con.cursor()

        cur.execute("DELETE from STUDENT where ADMISSION=3420;")
        con.commit()
        print("Total deleted rows:", cur.rowcount)

        cur.execute("SELECT admission, name, age, course, department from STUDENT")
        rows = cur.fetchall()
        for row in rows:
            print("ADMISSION =", row[0])
            print("NAME =", row[1])
            print("AGE =", row[2])
            print("COURSE =", row[3])
            print("DEPARTMENT =", row[4], "\n")

        print("Deletion successful")
        con.close()


    def Sql_Init(Name_DB):
        Name_DB = Name_DB + ".db"
        # with sqlite3.connect(Name_DB) as conn:
        #     c = conn.cursor()
        #
        #     # Create table nodes
        #     c.execute('''CREATE TABLE if not exists Node
        #                  (ID_Laser integer, Serial_Laser integer, Location text, Address_node text, Time_Pick_Data integer )''')
        #
        #     # Create table acount
        #     c.execute('''CREATE TABLE if not exists Acount
        #                  (ID_User integer, UserName text, Password text, Level integer, Name text, Family text )''')
        #
        #     # Create table queue
        #     c.execute('''CREATE TABLE if not exists Queue
        #                  (Num integer , Type text, ID integer, Command integer, Info text )''')
        #
        #     # Create table Raspberry
        #     c.execute('''CREATE TABLE if not exists Raspberry
        #                  (ID_Raspberry integer, Serial_Raspberry integer, Location text , Number_Node integer )''')
        #     conn.commit()


    def Sql_Init_Laser_Table(Name_DB, Laser_table):
        Name_DB = Name_DB + ".db"
        Laser_table = "Laser_" + Laser_table
        #
        # with sqlite3.connect(Name_DB) as conn:
        #     c = conn.cursor()
        #     # Create table
        #     sql = 'create table if not exists ' + Laser_table + ' (Data integer, Time text )'
        #     c.execute(sql)
        #     # Save (commit) the changes
        #     conn.commit()


    def Sq1_Fetch_Last(Name_DB, ID_Laser):
        Name_DB = Name_DB + ".db"
        # with sqlite3.connect(Name_DB) as conn:
        #     # mux data
        #     sql = "SELECT Data ,  MAX(Time) FROM Laser_" + ID_Laser
        #     cursor = conn.execute(sql)
        #     data = cursor.fetchone()
        #
        #     data_fetch = str(data[0]) + '|' + str(data[1])
        #     # return tupel

        return data_fetch
















class MongoDB:

    def Creating_Database():
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]

    def Creating_Collection():
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["customers"]


    def Check_Collection_Exists():
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        collist = mydb.list_collection_names()
        if "customers" in collist:
            print("The collection exists.")


    def Inserting_Data():
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["customers"]

        mydict = {"name": "John", "address": "Highway 37"}

        x = mycol.insert_one(mydict)



    def query():
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["customers"]

        myquery = {"address": "Park Lane 38"}

        mydoc = mycol.find(myquery)

        for x in mydoc:
            print(x)