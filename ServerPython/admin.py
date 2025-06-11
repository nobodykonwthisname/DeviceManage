from admin_sql import ConditionQueryBranch, ConditionQueryType, DelApplicaton, DelDevice, DeleUserDetail, DeleUserRegiste, StatusQueryType, UpdataApplicationData, UpdataUserData, deviceImformationAdd, getApplicationData, getFeedback, getUserData, userImformationAdd
from flask import Blueprint, request,json
manager_bp = Blueprint('manager', __name__, url_prefix='/manager')

'''添加新的设备'''
@manager_bp.route('/deviceDataAdd',methods=['POST','GET'])
def deviceDataAdd():
    Data=request.get_data(as_text=True)
    print('这是data',Data)
    AddData=json.loads(Data)
    numbering=AddData['numbering']
    nickname=AddData['nickname']
    deviceType=AddData['type']
    branch=AddData['branch']
    place=AddData['place']
    print('numbering,nickname,deviceType,branch,place',numbering,nickname,deviceType,branch,place)
    flag=deviceImformationAdd(numbering,nickname,deviceType,branch,place)
    if flag:
        res={
            'msg':'添加成功',
            'status':200
        }
    else:
        res={
             'msg':'添加失败',
            'status':0
        }
    return res

'''在管理员界面添加新用户'''
@manager_bp.route('/userDataAdd',methods=['POST','GET'])
def userDataAdd():
    Data=request.get_data(as_text=True)
    AddData=json.loads(Data)
    usename=AddData['usename']
    sex=AddData['sex']
    age=AddData['age']
    name=AddData['name']
    email=AddData['email']
    phonenumber=AddData['phonenumber']
    address=AddData['address']
    password=AddData['password']
    branch=AddData['branch']
    flag=userImformationAdd(name,password,email,phonenumber,branch,age,sex,address,usename)
    if flag:
        res={
            'msg':'添加成功',
            'status':200
        }
    else:
        res={
             'msg':'添加失败',
            'status':0
        }
    return res

'''在管理员界面激活新用户'''
@manager_bp.route('/userActiveAdd',methods=['POST','GET'])
def userActiveAdd():
    Data=request.get_data(as_text=True)
    AddData=json.loads(Data)
    name=AddData['name']
    usename=AddData['usename']
    password=AddData['password']
    branch=AddData['branch']
    email=''
    phonenumber=''
    address=''
    sex=''
    age=''
    flag=userImformationAdd(name,password,email,phonenumber,branch,age,sex,address,usename)
    if flag:
        res={
            'msg':'激活成功',
            'status':200
        }
    else:
        res={
             'msg':'添加失败',
            'status':0
        }
    return res

'''获取用户数据信息请求'''
@manager_bp.route('/getUsersData',methods=['POST','GET'])
def GetUsersData():
    res = getUserData()
    return res

'''获取用户反馈信息请求'''
@manager_bp.route('/getFeedbackData',methods=['POST','GET'])
def getFeedbackData():
    res = getFeedback()
    return res

'''获取用户申请表数据信息请求'''
@manager_bp.route('/getApplicationData',methods=['POST','GET'])
def GetApplicationData():
    res = getApplicationData()
    return res

'''√删除指定usename和numbering的请求（包括拒绝用户注册和管理员主动删除用户，删除设备信息）'''
@manager_bp.route('/delete',methods=['POST','GET'])
def DeleteMessage():
    Data=request.get_data(as_text=True)
    DeleteData=json.loads(Data)
    pri=DeleteData['pri']
    if(pri==0):
            usename=DeleteData['usename']
            DeleUserDetail(usename)
    elif(pri==1):
            usename=DeleteData['usename']
            DeleUserRegiste(usename)
    elif(pri==2):
            ###删除制定的numbering的申请表信息
            numbering=DeleteData['numbering']
            DelApplicaton(numbering)
    elif(pri==3):
            ###删除设备信息
            numbering=DeleteData['numbering']
            DelDevice(numbering)
    res={
        'msg':'删除成功',
        'status':200
    }
    return res

'''更新指定usename的请求'''
@manager_bp.route('/updateUser',methods=['POST','GET'])
def updateData():
    Data=request.get_data(as_text=True)
    info=json.loads(Data)
    usename=info['usename']
    sex=info['sex']
    age=info['age']
    name=info['name']
    email=info['email']
    phonenumber=info['phonenumber']
    address=info['address']
    password=info['password']
    branch=info['branch']
    UpdataUserData(name,password,email,phonenumber,branch,age,sex,address,usename)
    res={
        'msg':'修改成功',
        'status':200
    }
    return res

####################################################设备方面#######################################################
'''用于获取按部门分的设备信息'''
@manager_bp.route('/getEquipmentBranchData',methods=['POST','GET'])
def GetEquipmentBranchData():
    Data=request.get_data(as_text=True)
    EquimentData=json.loads(Data)
    branch=EquimentData['branch']
    res =ConditionQueryBranch(branch)
    return res

'''删除设备请求在用户的DeleteMessage那一块'''

'''用于获取按设备类型分的设备信息'''
@manager_bp.route('/getEquipmentTypeData',methods=['POST','GET'])
def GetEquipmentTypeData():
    Data=request.get_data(as_text=True)
    EquimentData=json.loads(Data)
    EquipmentType=EquimentData['EquipmentType']
    res =ConditionQueryType(EquipmentType)
    return res

'''用于获取按设备状态分的设备信息'''
@manager_bp.route('/getEquipmentStatusData',methods=['POST','GET'])
def GetEquipmentStatusData():
    Data=request.get_data(as_text=True)
    EquimentData=json.loads(Data)
    EquipmentStatus=EquimentData['status']
    res =StatusQueryType(EquipmentStatus)
    return res

'''申请同意后修改设备状态'''
@manager_bp.route('/updateApplication',methods=['POST','GET'])
def updateApplication():
    Data=request.get_data(as_text=True)
    info=json.loads(Data)
    numbering=info['numbering']
    UpdataApplicationData(numbering)
    res={
        'msg':'修改成功',
        'status':200
    }
    return res

'''添加新的设备'''
@manager_bp.route('/deviceDataAdd',methods=['POST','GET'])
def deviceDataAdd():
    Data=request.get_data(as_text=True)
    print('这是data',Data)
    AddData=json.loads(Data)
    numbering=AddData['numbering']
    nickname=AddData['nickname']
    deviceType=AddData['type']
    branch=AddData['branch']
    place=AddData['place']
    print('numbering,nickname,deviceType,branch,place',numbering,nickname,deviceType,branch,place)
    flag=deviceImformationAdd(numbering,nickname,deviceType,branch,place)
    if flag:
        res={
            'msg':'添加成功',
            'status':200
        }
    else:
        res={
             'msg':'添加失败',
            'status':0
        }
    return res

