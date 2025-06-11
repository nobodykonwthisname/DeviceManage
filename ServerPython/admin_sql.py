import pymysql  
import json

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

#检验管理员的账号是否有用
def LoginVerify(usename,password):
    cursor=ConnectSql()
    sql='select * from manager where usename=%s'
    cursor.execute(sql,(usename,))
    res=cursor.fetchall()
    #验证是不是管理员
    if res:
        real_dict=res[0]
        if password==real_dict[2]:
            return ({'role':'manager'})
        else:
            return False
    else:
        #验证是不是用户
        sql2='select * from usermessage where usename=%s'
        cursor.execute(sql2,(usename,))
        res=cursor.fetchall()
        if res:
            real_dict=res[0]
            if password==real_dict[1]:
                return ({'role':'user'})
            else:
                return False

###########################################################用户管理方面################################################
#增①：用户注册登记
def AddUser(usename,password,email):
    cursor=ConnectSql()
    sql='insert into userregister(usename,password,email) values(%s,%s,%s)' 
    values=(usename,password,email)
    cursor.execute(sql,values)
    cursor.connection.commit()
     # 关闭数据库连接
    cursor.close()
    return True

#增②:用户注册登记
def userImformationAdd(name,password,email,phonenumber,branch,age,sex,address,usename):
    cursor=ConnectSql()
    sql='insert into usermessage(name,password,email,phonenumber,branch,age,sex,address,usename) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    values=(name,password,email,phonenumber,branch,age,sex,address,usename)
    cursor.execute(sql,values)
    cursor.connection.commit()
     # 关闭数据库连接
    cursor.close()
    return True

#删：删除指定的一条数据
def DeleUserDetail(usename):
    cursor=ConnectSql()
    sql='delete from usermessage where usename=%s'
    cursor.execute(sql,usename)
    cursor.connection.commit()
    cursor.close()
    return True

#删：拒绝指定用户的注册申请
def DeleUserRegiste(usename):
    cursor=ConnectSql()
    sql='delete from userregister where usename=%s'
    cursor.execute(sql,usename)
    cursor.connection.commit()
    cursor.close()
    return True

#改：修改用户信息    
def UpdataUserData(name,password,email,phonenumber,branch,age,sex,address,usename):
    cursor=ConnectSql()
    sql='update usermessage set name=%s, password=%s,email=%s,phonenumber=%s, branch=%s ,age=%s,sex=%s,address=%s where usename=%s'
    values=(name,password,email,phonenumber,branch,age,sex,address,usename)
    cursor.execute(sql,values)
    cursor.connection.commit()
    cursor.close()
    return True

#查：查询指定用户的信息
def SearchUserData(name):
    cursor=ConnectSql()
    sql='select * from usermessage where name=%s'
    result=cursor.execute(sql,name)
    #获取所有行
    result=cursor.fetchall()
    #res=json.dumps(result)
    jsonData=[]
    #将获取的数据库的信息转化为json
    for row in result:
        res={}
        res['name']=(row[0])
        res['password']=(row[1])
        res['email']=(row[2])
        res['phonenumber']=(row[3])
        res['branch']=(row[4])
        res['tel']=(row[5])
        res['address']=(row[6])
        res['usename']=(row[7])
        jsonData.append(res)
    return(jsonData)

#展示数据库user的五条信息
def getUserData():
    cursor=ConnectSql()
    sql='select * from usermessage'
    result=cursor.execute(sql)
    #获取所有行
    result=cursor.fetchall()
    #res=json.dumps(result)
    jsonData=[]
    #将获取的数据库的信息转化为json
    for row in result:
        res={}
        res['name']=(row[0])
        res['password']=(row[1])
        res['email']=(row[2])
        res['phonenumber']=(row[3])
        res['branch']=(row[4])
        res['tel']=(row[5])
        res['address']=(row[6])
        res['usename']=(row[7])
        res['sex']=(row[8])
        res['age']=(row[9])
        jsonData.append(res)
    return(jsonData)

#展示数据库userapplication的数据
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
    return(jsonData)

#展示数据库用户注册的信息
def getRegistersData():
    cursor=ConnectSql()
    sql='select * from userregister'
    result=cursor.execute(sql)
    #获取所有行
    result=cursor.fetchall()
    #res=json.dumps(result)
    jsonData=[]
    for row in result:
        res={}
        res['name']=(row[0])
        res['usename']=(row[1])
        res['password']=(row[2])
        res['branch']=(row[3])
        
        jsonData.append(res)
    return(jsonData)

#展示反馈信息
def getFeedback():
    cursor=ConnectSql()
    sql='select * from feedback'
    result=cursor.execute(sql)
    #获取所有行
    result=cursor.fetchall()
    #res=json.dumps(result)
    jsonData=[]
    for row in result:
        res={}
        res['name']=(row[0])
        res['usename']=(row[1])
        res['content']=(row[2])
        jsonData.append(res)
    return(jsonData)

###########################################################设备管理方面###################################################
#根据不同部门查询信息
def ConditionQueryBranch(branch):
    #连接数据库
    cursor=ConnectSql()
    sql='select * from application where branch=%s'
    result=cursor.execute(sql,branch)
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

#根据不同设备类型查询信息
def ConditionQueryType(applicationType):
    #连接数据库
    cursor=ConnectSql()
    sql='select * from application where type=%s'
    result=cursor.execute(sql,applicationType)
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

#根据不同状态查询信息
def StatusQueryType(status):
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

#删除指定numbering的申请信息
def DelApplicaton(numbering):
    cursor=ConnectSql()
    sql='delete from userapplication where numbering=%s'
    cursor.execute(sql,numbering)
    cursor.connection.commit()
    cursor.close()
    return True

#删除指定numbering的设备信息
def DelDevice(numbering):
    cursor=ConnectSql()
    sql='delete from application where numbering=%s'
    cursor.execute(sql,numbering)
    cursor.connection.commit()
    cursor.close()
    return True

#更改指定设备的状态
def UpdataApplicationData(numbering):
    cursor=ConnectSql()
    sql="update application set status='在用' where numbering=%s"
    cursor.execute(sql,numbering)
    cursor.connection.commit()
    cursor.close()
    return True

#添加新设备信息
def deviceImformationAdd(numbering,nickname,detype,branch,place):
    cursor=ConnectSql()
    count=1
    status='闲置'
    maintenance=0
    used=0
    sql='insert into application(numbering,nickname,type,branch,place, count,status,maintenance,used) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)' 
    values=(numbering,nickname,detype,branch,place, count,status,maintenance,used)
    cursor.execute(sql,values)
    cursor.connection.commit()
     # 关闭数据库连接
    cursor.close()
    return True

# 获取echarts展示的数据
def getechartsData(branch):
    cursor=ConnectSql()
    sql="SELECT SUM(used) AS used_total, SUM(maintenance) AS maintenance_total FROM application WHERE branch = %s AND type = (SELECT type FROM application WHERE branch = %s LIMIT 1)"
    values=(branch,branch)
    res=cursor.execute(sql,values)
    res=cursor.fetchall()
    return res