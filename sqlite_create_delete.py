import sqlite3
 
db = sqlite3.connect('friends.db')
 
db.execute('drop table if exists friends')
 
db.execute('create table friends (i int, friend text)')
 
db.execute('insert into friends(i, friend) values (?,?)', ( 1, 'Shubo ' ))
db.execute('insert into friends(i, friend) values (?,?)', ( 2, 'Tuhin ' ))
db.execute('insert into friends(i, friend) values (?,?)', ( 3, 'Tanvir ' ))
db.execute('insert into friends(i, friend) values (?,?)', ( 4, 'Dipu ' ))
db.execute('insert into friends(i, friend) values (?,?)', ( 5, 'Siyam ' ))
db.commit()
 
print ("nBefore delete: n" )
result = db.execute('select * from friends')
for row in result :
    print (row)
    
db.execute('delete from friends where i = 1' )
db.commit()
 
print ("n After delete: n" )
result = db.execute('select * from friends')
for row in result :
    print (row)
