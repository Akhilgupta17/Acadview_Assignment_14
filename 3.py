import pymysql as pm

try:
    con = pm.connect(host='localhost', database='Akhildb',\
                     user='root', password='root')
    
    cursor = con.cursor()

    query="select * from Authors_Titles"

    cursor.execute(query)
    data=cursor.fatchall()
    print('Authors_Title_ID: {}, AuthorID: {}, TitleId: {}'.format(row[0], row[1], row[2]))
    
    query1= "update Authors_Titles set AuthorID=AuthorID+1 where AuthoerId = 10001 "
    
    cursor.execute(query1)
    data1=cursor.fatchall()
    print('Authors_Title_ID: {}, AuthorID: {}, TitleId: {}.format(row[0], row[1], row[2]))
    
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