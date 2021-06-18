import sqlite3

# link to SQLite database namded mrsoft.db
conn = sqlite3.connect('mrsoft.db')
# create a cursor object
cursor = conn.cursor()
# execute a SQL statement to create a user table
try:
    cursor.execute('create table user (id int(10) primary key, name varchar(20))')
except:
    print('user table has been created')

# add user data
cursor.execute('insert into user (id,name) values ("1","ethan")')
# view user data
cursor.execute('select * from user')
result1 = cursor.fetchone()
print(result1)
# update user data
cursor.execute('update user set name =? where id=?',('xieruifeng',1))
cursor.execute('select * from user')
result1 = cursor.fetchone()
print(result1)
# delete user data
cursor.execute('delete from user where id=?',(1,))
cursor.execute('select * from user')
result1 = cursor.fetchone()
print(result1)
# close cursor
cursor.close()
# commit work
conn.commit()
# close connection
conn.close()
