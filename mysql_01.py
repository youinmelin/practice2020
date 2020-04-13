from pymysql import connect 

conn = connect(host='localhost',port=3306,user='youinme',password='123456',database='youinme',charset='utf8')
cursor = conn.cursor()
sql = 'select * from message;'
ret = cursor.execute(sql)
# fetchall() fetchmany(num) fetchone()
content = cursor.fetchall()
print (ret)
print (content)
sql = ' delete from message where uname="XXX";' 
ret = cursor.execute(sql)
print (ret)
cursor.close()
conn.close()

