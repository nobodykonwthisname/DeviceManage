import pymysql  

#连接数据库
def ConnectSql():
    # 打开数据库连接
    conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='12345678',
                       charset = 'utf8'
                       )
                
    # 使用 cursor() 方法创建一个游标对象 cursor                      
    cursor = conn.cursor()
    # 使用 execute()  方法执行 SQL 查询
    cursor.execute("use DeviceDesign;")
    return cursor

#申请(申请表信息展示)展示数据库userapplication的数据
def getApplicationData():
    cursor=ConnectSql()
    sql='select * from userapplication'
    result=cursor.execute(sql)
    #获取所有行
    result=cursor.fetchall()
    #res=json.dumps(result)
    jsonData=[]
    #将获取的数据库的信息转化为json
    for row in result:
        res={}
        res['name']=(row[0])
        res['branch']=(row[1])
        res['numbering']=(row[2])
        res['nickname']=(row[3])
        res['count']=(row[4])
        res['place']=(row[5])
        jsonData.append(res)
    return (jsonData)

#归还(租借表信息展示)展示数据库own的数据
def getOwnData():
    cursor=ConnectSql()
    sql='select * from own'
    result=cursor.execute(sql)
    #获取所有行
    result=cursor.fetchall()
    #res=json.dumps(result)
    jsonData=[]
    #将获取的数据库的信息转化为json
    print(result)
    for row in result:
        res={}
        res['username']=(row[0])
        res['numbering']=(row[1])
        res['nickname']=(row[2])
        res['phone']=(row[3])
        res['place']=(row[4])
        res['count']=(row[5])
        jsonData.append(res)
    return jsonData 

#报修(故障表申请展示)展示数据库repairs的数据
def getRepairsData():
    cursor=ConnectSql()
    sql='select * from repairs'
    result=cursor.execute(sql)
    #获取所有行
    result=cursor.fetchall()
    #res=json.dumps(result)
    jsonData=[]
    #将获取的数据库的信息转化为json
    print(result)
    for row in result:
        res={}
        res['numbering']=(row[0])
        res['nickname']=(row[1])
        res['situation']=(row[2])
        jsonData.append(res)
    return jsonData

#(展示application里面的闲置设备信息)
def getUnusedApplication(status):
    #连接数据库
    cursor=ConnectSql()
    sql='select * from application where status=%s'
    result=cursor.execute(sql,status)
    #获取所有行
    result=cursor.fetchall()
    #res=json.dumps(result)
    jsonData=[]
    for row in result:
        res={}
        res['numbering']=(row[0])
        res['nickname']=(row[1])
        res['type']=(row[2])
        res['branch']=(row[3])
        res['place']=(row[4])
        res['count']=(row[5])
        res['status']=(row[6])
        res['maintenance']=(row[7])
        res['used']=(row[8])
        jsonData.append(res)
    return jsonData

#(展示application里面的在用设备信息，暂定没写指定usename)
def getReturnApplication():
    #连接数据库
    cursor=ConnectSql()
    sql='select * from userapplication '
    result=cursor.execute(sql)
    #获取所有行
    result=cursor.fetchall()
    #res=json.dumps(result)
    jsonData=[]
    print(result)
    for row in result:
        res={}
        res['name']=(row[0])
        res['branch']=(row[1])
        res['numbering']=(row[2])
        res['nickname']=(row[3])
        res['count']=(row[4])
        res['place']=(row[5])
        res['usename']=(row[6])
        res['status']=(row[7])
        jsonData.append(res)
    return (jsonData)

#(删除申请表该用户指定的设备申请)
def deleteReturn(numbering):
    cursor=ConnectSql()
    sql='delete from userapplication where numbering=%s'
    cursor.execute(sql,numbering)
    cursor.connection.commit()
    cursor.close()
    return True

#(删除在用表的numbering信息)
def deleteOwn(numbering):
    cursor=ConnectSql()
    sql='delete from own where numbering=%s'
    cursor.execute(sql,numbering)
    cursor.connection.commit()
    cursor.close()
    return True

# 更新指定numbering的status
def upApplicationData(numbering):
    cursor=ConnectSql()
    status='闲置'
    sql='update application set status=%s where numbering=%s'
    values=(status,numbering)
    cursor.execute(sql,values)
    cursor.connection.commit()
    cursor.close()
    return True

# 更新个人信息（usermessage）
def updateUser(name,password,email,phonenumber,branch,address,usename,sex,age):
    cursor=ConnectSql()
    sql='update usermessage set name=%s, password=%s,email=%s,phonenumber=%s, branch=%s,address=%s ,sex=%s,age=%s where usename=%s'
    values=(name,password,email,phonenumber,branch,address,sex,age,usename)
    cursor.execute(sql,values)
    cursor.connection.commit()
    cursor.close()
    return True

# 添加application信息
def addApply(numbering,name,branch,nickname,count,place,usename,status):
    cursor=ConnectSql()
    sql='insert into application(numbering,name,branch,nickname,count,place,usename,status) values(%s,%s,%s,%s,%s,%s,%s,%s)' 
    values=(numbering,name,branch,nickname,count,place,usename,status)
    cursor.execute(sql,values)
    cursor.connection.commit()
    cursor.close()
    return True
