from flask import Blueprint, jsonify,request,json

from user_sql import getApplicationData,getOwnData,getRepairsData,getUnusedApplication,getReturnApplication,deleteReturn,deleteOwn
from user_sql import upApplicationData,addApply,updateUser
user_bp = Blueprint('user', __name__, url_prefix='/user')

# 用户请求：展示申请表信息
@user_bp.route('/getApplicationData', methods=['POST','GET'])
def GetApplicationData():
    res = getApplicationData()
    return res

# 用户请求：展示在用表信息
@user_bp.route('/getOwnData', methods=['POST','GET'])
def GetOwnData():
    res = getOwnData()
    return res

# 用户请求：展示报修表信息
@user_bp.route('/getRepairsData', methods=['POST','GET'])
def GetRepairsData():
    res = getRepairsData()
    return res

# 用户请求：展示可申请使用设备信息
@user_bp.route('/getUnusedApplication', methods=['POST','GET'])
def GetUnusedApplication():
    res = getUnusedApplication('闲置')
    print('来自getUnusedApplication',res)
    return res

# 用户请求：展示可归还设备信息
@user_bp.route('/getReturnApplication', methods=['POST','GET'])
def GetReturnApplication():
    res = getReturnApplication()
    return res

# 删除请求：删除指定设备编号的信息（application表里面）
@user_bp.route('/deleteReturnApplication', methods=['POST','GET'])
def DeleteReturnApplication():
    Data=request.get_data(as_text=True)
    DeleteData=json.loads(Data)
    numbering=DeleteData['numbering']
    deleteReturn(numbering)
    res={
        'msg':'删除成功',
        'status':200
    }
    return res

# 删除请求：（own表里面）
@user_bp.route('/deleteOwn', methods=['POST','GET'])
def DeleteOwn():
    Data=request.get_data(as_text=True)
    DeleteData=json.loads(Data)
    numbering=DeleteData['numbering']
    flag=deleteOwn(numbering)
    upApplicationData(numbering)
    if flag:
        res={
        'msg':'删除成功',
        'status':200
    }
    return res

# 添加请求(application)：
@user_bp.route('/addApply', methods=['POST','GET'])
def AddApply():
    Data=request.get_data(as_text=True)
    AddData=json.loads(Data)
    numbering=AddData['numbering']
    name=AddData['name']
    branch=AddData['branch']
    nickname=AddData['nickname']
    count=AddData['count']
    place=AddData['place']
    usename=AddData['usename']
    status=AddData['status']
    flag=addApply(numbering,name,branch,nickname,count,place,usename,status)
    if flag:
        res={
        'msg':'添加成功',
        'status':200
    }
    return res

#修改请求（usermessage）
@user_bp.route('/updateUser', methods=['POST','GET'])
def UpdateUser():
    Data=request.get_data(as_text=True)
    userData=json.loads(Data)
    name=userData['name']
    password=userData['password']
    email=userData['email']
    phonenumber=userData['phonenumber']
    branch=userData['branch']
    tel=userData['tel']
    address=userData['address']
    usename=userData['usename']
    sex=userData['sex']
    age=userData['age']
    flag=updateUser(name,password,email,phonenumber,branch,tel,address,usename,sex,age)
    if flag:
        res={
        'msg':'修改个人信息成功',
        'status':200
    }
    return res