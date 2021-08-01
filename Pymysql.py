import pymysql
from app import User,users



def loginInquire():
    conn = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='Wswql123',
        db='user',
        charset='utf8'
    )

    cur = conn.cursor()
    sql = "select * from userInfor"
    cur.execute(sql)
    content = cur.fetchall()
    #

    # insertSql= "INSERT INTO userInfor (tel, userName, password) VALUES(15385779612,'吴其亮','wswql')"
    # cur.execute(insertSql)
    for i in  content:
        print(i[0],i[1],i[2])
        users.append(User(i[0],i[1],i[2]))
    return users

