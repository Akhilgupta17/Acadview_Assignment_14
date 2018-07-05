import pymysql as pm
try:
    con = pm.connect(host='localhost', database='Akhildb', user='root', password='root')
    cursor = con.cursor()
    query6= "insert into Authors(AuthorID,FirstName,MiddleName,LastName) values(10001,'Ram','kumar','verma')"
    cursor.execute(query6)
    query4= "insert into Zip_Codes(Zip_Code_ID,City,State,Zip_Code) values(101,'Mumbai','Maharasthra',501)"
    cursor.execute(query4)
    query3= "insert into Publishers(Publisher_ID,Name,Street_Address,Suite_Number,Zip_Code_ID) values(601,'Krishna','12/24 BasantBihar',11,101)"
    cursor.execute(query3)
    query2= "insert into Titles(TitleID,Title,ISBN,Publisher_ID,Publication_Year) values(701,'Science',978-3-16-148410-0, 601,2017)"
    cursor.execute(query2)
    query1= "insert into Books(BookId, TitleId, Location, Genre) values(1001, 701, 'Delhi','Science')"
    cursor.execute(query1)
    query5= "insert into Authors_Titles(Author_Title_ID,AuthorID,TitleId) values(1,10001,701)"
    cursor.execute(query5)
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
