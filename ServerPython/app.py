from flask import Flask, json, request
#解决跨域问题
from flask_cors import CORS
#引入sql文件里的方法
from admin_sql import LoginVerify,AddUser,getUserData,getApplicationData,DeleUserDetail,deviceImformationAdd
from admin_sql import DeleUserRegiste,getFeedback,ConditionQueryBranch,ConditionQueryType,DelDevice,StatusQueryType
from admin_sql import UpdataUserData,userImformationAdd,getRegistersData,DelApplicaton,UpdataApplicationData
import jwt
import datetime
#引入用户请求蓝图
from user import user_bp
DEBUG = True

'''在python中带着@的基本上是装饰器，装饰器的本质是扩展原函数功能的一种函数
    @app.route('url')就是程序运行起来，然后输入这里的url，页面上显示的是这里的return值

    注意事项：
    在app.route(’/TestB/’)中，TestB前后有斜杆，则访问时，是否在TestB后面加斜杠，Flask都会重定向到(/TestB/)中，且访问成功，
    若在app.route(’/TestA`)，TestA后无斜杠，则在访问时，则在访问时，若访问(/TestA/)，则会报错，访问(/TestA)，则访问成功

'''
app = Flask(__name__)
app.register_blueprint(user_bp)
app.config.from_object(__name__)

CORS(app,supports_credentials=True)

# 生成 Token
def generate_token(payload, secret_key, expire):
    payload['exp'] = datetime.datetime.utcnow() + datetime.timedelta(seconds=expire)
    
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    token=token.encode('utf-8').decode("unicode-escape")
    return token

# 验证身份
def verify_identity(req):
    auth_header = req.headers.get('Authorization')
    if auth_header:
        # 获取 Token
        token = auth_header.split(' ')[1]
        try:
            # 解析 Token
            payload = jwt.decode(token, 'your_secret_key', algorithms=['HS256'])
            usename = payload.get('usename')
            role = payload.get('role')

            # 验证身份
            if usename and role == 'user':
                return {'status': 200, 'msg': '验证成功'}
            elif usename and role == 'manager':
                return {'status': 200, 'msg': '验证成功'}
            else:
                return {'status': 403, 'msg': '无权限访问'}
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return {'status': 401, 'msg': 'Token 已过期或无效'}
    else:
        return {'status': 401, 'msg': '缺少 Token'}



'''return只能返回字符类型或者是字典'''
'''验证普通用户的账号密码'''
@app.route('/login', methods=['POST', 'GET'])
def login():
    a=request.get_data(as_text=True)
    b=json.loads(a)
    usename=b['usename']
    password=int(b['password'])
    flag=LoginVerify(usename,password)
    print(flag['role'])
    if flag['role']=='user':
        # 生成 Token 并返回
        
        token = generate_token({'usename': usename, 'role': 'user'}, 'your_secret_key', 3600)
        res={
            'msg':'登录成功',
            'role':'user',
            'status':200,
            'token': token           
        }
    elif flag['role']=='manager':
        # 生成 Token 并返回
        token = generate_token({'usename': usename, 'role': 'manager'}, 'your_secret_key', 3600)
        res={
             'msg':'登录成功',
            'role':'manager',
            'status':200,
            'token': token
        }
    else:
         res={
              'msg':'登录失败',
              'status':0
         }
    return json.dumps(res)

'''注册请求'''
@app.route('/register',methods=['POST','GET'])
def register():
    Data=request.get_data(as_text=True)
    RegisterData=json.loads(Data)
    usename=RegisterData['usename']
    password=RegisterData['password']
    email=RegisterData['email']
    flag=AddUser(usename,int(password),email)
    if flag:
        res={
            'msg':'注册成功',
            'status':1
        }
    else:
        res={
             'msg':'注册失败',
            'status':0
        }
    return res

###################################################用户方面############################################################
'''在管理员界面添加新用户'''
@app.route('/userDataAdd',methods=['POST','GET'])
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
@app.route('/userActiveAdd',methods=['POST','GET'])
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
@app.route('/getUsersData',methods=['POST','GET'])
def GetUsersData():
    res = getUserData()
    return res

'''获取用户反馈信息请求'''
@app.route('/getFeedbackData',methods=['POST','GET'])
def getFeedbackData():
    res = getFeedback()
    return res

'''获取用户申请表数据信息请求'''
@app.route('/getApplicationData',methods=['POST','GET'])
def GetApplicationData():
    res = getApplicationData()
    return res

'''用于获取待激活的用户信息'''
@app.route('/getRegistersData',methods=['POST','GET'])
def GetRegistersData():
    res =getRegistersData()
    return res

'''√删除指定usename和numbering的请求（包括拒绝用户注册和管理员主动删除用户，删除设备信息）'''
@app.route('/delete',methods=['POST','GET'])
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
@app.route('/updateUser',methods=['POST','GET'])
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
@app.route('/getEquipmentBranchData',methods=['POST','GET'])
def GetEquipmentBranchData():
    Data=request.get_data(as_text=True)
    EquimentData=json.loads(Data)
    branch=EquimentData['branch']
    res =ConditionQueryBranch(branch)
    return res

'''删除设备请求在用户的DeleteMessage那一块'''

'''用于获取按设备类型分的设备信息'''
@app.route('/getEquipmentTypeData',methods=['POST','GET'])
def GetEquipmentTypeData():
    Data=request.get_data(as_text=True)
    EquimentData=json.loads(Data)
    EquipmentType=EquimentData['EquipmentType']
    res =ConditionQueryType(EquipmentType)
    return res

'''用于获取按设备状态分的设备信息'''
@app.route('/getEquipmentStatusData',methods=['POST','GET'])
def GetEquipmentStatusData():
    Data=request.get_data(as_text=True)
    EquimentData=json.loads(Data)
    EquipmentStatus=EquimentData['status']
    res =StatusQueryType(EquipmentStatus)
    return res

'''申请同意后修改设备状态'''
@app.route('/updateApplication',methods=['POST','GET'])
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
@app.route('/deviceDataAdd',methods=['POST','GET'])
def deviceDataAdd():
    Data=request.get_data(as_text=True)
    print('这是data',Data)
    AddData=json.loads(Data)
    numbering=AddData['numbering']
    nickname=AddData['nickname']
    deviceType=AddData['type']
    branch=AddData['branch']
    place=AddData['place']
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

if __name__ == '__main__':
    app.run()