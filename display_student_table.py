import pymysql as py
con = py.connect(host="localhost",user="root",password="",database="school")
cur = con.cursor()
cur.execute("SELECT * FROM student")

rows = cur.fetchall()
for row in rows:
    print(row)



con.close()


