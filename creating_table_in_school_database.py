import pymysql as py
mydatabase=py.connect(host="localhost",user="root",password="",database="school")
    #Table student (st_id,st_name,st_class,st_email)
mytable=mydatabase.cursor()
try:
    tc = "CREATE TABLE student(st_id INT PRIMARY KEY AUTO_INCREMENT, st_name VARCHAR(50), st_email VARCHAR(50))"
    mytable.execute(tc)
    mydatabase.commit()
    mydatabase.close()
except Exception as e:
    print("Error while connecting or executing SQL:")
    print(e)