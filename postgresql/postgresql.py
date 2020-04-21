
import psycopg2

from config import config

#https://stackabuse.com/working-with-postgresql-in-python/
#https://www.postgresqltutorial.com/postgresql-python/call-stored-procedures/

#https://thoughtbot.com/blog/reading-an-explain-analyze-query-plan


def connect():

    """this is use file ini  and config adn library config"""
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()


        cur.execute('''CREATE TABLE if not exists STUDENT
              (ADMISSION INT      NOT NULL,
              NAME           TEXT    NOT NULL,
              AGE            INT     NOT NULL,
              COURSE        CHAR(50),
              DEPARTMENT        CHAR(50));''')

        conn.commit()

        cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')")
        conn.commit()


        cur.execute("EXPLAIN ANALYZE SELECT admission, age, name, course, department from STUDENT")
        rows = cur.fetchall()

        for row in rows:
            print("ADMISSION =", row[0])
            print("NAME =", row[1])
            print("AGE =", row[2])
            print("COURSE =", row[2])
            print("DEPARTMENT =", row[3], "\n")

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def EXPLAIN_ANALYZE_table():
    # read connection parameters
    params = config()

    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**params)

    # create a cursor
    cur = conn.cursor()

    cur.execute("EXPLAIN ANALYZE SELECT admission, age, name, course, department from STUDENT")
    rows = cur.fetchall()


if __name__ == '__main__':
    connect()
    EXPLAIN_ANALYZE_table()
