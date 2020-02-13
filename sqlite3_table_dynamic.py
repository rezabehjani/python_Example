import sqlite3

location = 'sql.db'
table_name = 'devise'

conn = sqlite3.connect(location)
c = conn.cursor()

sql = 'create table if not exists ' + table_name + ' (id integer)'
c.execute(sql)


sql = 'insert into ' + table_name + ' (id) values (%d)' % (1)
c.execute(sql)
conn.commit()