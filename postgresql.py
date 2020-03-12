
import psycopg2


#https://stackabuse.com/working-with-postgresql-in-python/
#https://www.postgresqltutorial.com/postgresql-python/call-stored-procedures/



user_postgres = "postgres"
password_postgres = "19972910"
host_postgres = "127.0.0.1"
port_postgres = "5432"
database_postgres = "postgres"

# in psycopg2      not question mark ?????????  work   use %s %s %s %s %s %s  for plase holder 

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









def use_all():
    con = psycopg2.connect(database=database_postgres, user=user_postgres, password=password_postgres, host=host_postgres, port=port_postgres)
    print("Database opened successfully")
    cur = con.cursor()

    ##########################################
    cur.execute('''CREATE TABLE STUDENT
          (ADMISSION INT      NOT NULL,
          NAME           TEXT    NOT NULL,
          AGE            INT     NOT NULL,
          COURSE        CHAR(50),
          DEPARTMENT        CHAR(50));''')
    con.commit()
    ##########################################


    cur.execute("SELECT admission, name, age, course, department from STUDENT")
    rows = cur.fetchall()
    for row in rows:
        print("ADMISSION =", row[0])
        print("NAME =", row[1])
        print("AGE =", row[2])
        print("COURSE =", row[3])
        print("DEPARTMENT =", row[4], "\n")

    ##########################################
    cur.execute("UPDATE STUDENT set AGE = 20 where ADMISSION = 3420")
    con.commit()
    print("Total updated rows:", cur.rowcount)


    ###############################################
    cur.execute("SELECT admission, age, name, course, department from STUDENT")
    rows = cur.fetchall()
    for row in rows:
        print("ADMISSION =", row[0])
        print("NAME =", row[1])
        print("AGE =", row[2])
        print("COURSE =", row[2])
        print("DEPARTMENT =", row[3], "\n")

    ###############################################
    cur.execute(
        "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')")

    con.commit()

    cur.execute("SELECT admission, age, name, course, department from STUDENT")
    rows = cur.fetchall()
    for row in rows:
        print("ADMISSION =", row[0])
        print("NAME =", row[1])
        print("AGE =", row[2])
        print("COURSE =", row[2])
        print("DEPARTMENT =", row[3], "\n")

    ###############################################


    cur.execute("DELETE from STUDENT where ADMISSION=3420;")
    con.commit()
    print("Total deleted rows:", cur.rowcount)


    print("Deletion successful")
    con.close()


def EXPLAIN_ANALYZE_table():

    con = psycopg2.connect(database=database_postgres, user=user_postgres, password=password_postgres,
                           host=host_postgres, port=port_postgres)
    print("Database opened successfully")
    cur = con.cursor()


    cur.execute("EXPLAIN ANALYZE SELECT admission, age, name, course, department from STUDENT")
    rows = cur.fetchall()



if __name__ == '__main__':


    EXPLAIN_ANALYZE_table()