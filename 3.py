import pymysql as pm

try:
    con = pm.connect(host='localhost', database='Akhildb',\
                     user='root', password='root')
    
    cursor = con.cursor()

    query="select * from Authors"

    cursor.execute(query)
    data=cursor.fetchall()
    for row in data:
        print('AuthorID: {}, FirstName: {} MiddleName:{},LastName:{}'.format(row[0], row[1], row[2],row[3]))
    
    query1= "update Authors set FirstName='shivam' "
    
    cursor.execute(query1)
    
    data1=cursor.fetchall()
    for row in data1:
        print('AuthorID: {}, FirstName: {} MiddleName:{},LastName:{}'.format(row[0], row[1], row[2],row[3]))
    
    con.commit()
    
except pm.DatabaseError as e:
    if con:
        con.rollback()
        print('Problem occured: ', e)
    
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
    print('DONE!!')
