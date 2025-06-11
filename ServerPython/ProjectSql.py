from sqlalchemy import ForeignKey, create_engine, Column, Integer, String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
# 创建连接引擎
engine = create_engine('mysql+pymysql://root:12345678@host:port/devicedesign')

# 创建基类
Base = declarative_base()

# 定义设备表
class Application(Base):
    __tablename__ = 'application'
    numbering = Column(String(50),  primary_key=True)
    nickname = Column(String(50), nullable=False)
    status = Column(String(20), nullable=False)
    type=Column(String(20), nullable=False)
    branch=Column(String(20), nullable=False)
    place=Column(String(50), nullable=False)
    count = Column(Integer, default=0)
    used = Column(String(10))
    maintenance=Column(String(50), nullable=False)

# 定义 反馈信息表
class Application(Base):
    __tablename__ = 'feedback'
    usename = Column(String(20), primary_key=True)
    name=Column(String(20), nullable=False)
    content = Column(String(500), nullable=False)
    time = Column(DateTime, default=datetime.now)

# 定义 管理员信息表
class Application(Base):
    __tablename__ = 'manager'
    usename = Column(String(20), primary_key=True)
    name=Column(String(20), nullable=False)
    password = Column(Integer, default=0)

#定义租借信息表
class own(Base):
    __tablename__ = 'own'
    numbering=Column(String(20), primary_key=True)
    usename=Column(String(20), ForeignKey('usermessage.usename'))
    nickname=Column(String(20), nullable=False)
    place=Column(String(100), nullable=False)
    count= Column(Integer, default=0)

#定义 报修表
class repairs(Base):
    __tablename__='repairs'
    numbering=Column(String(20), primary_key=True)
    nickname=Column(String(20), nullable=False)
    sitution=Column(String(500), nullable=False)

#定义设备申请表
class userapplication(Base):
    __tablename__='userapplication'
    numbering=Column(String(20), primary_key=True)
    usename = Column(String(20), ForeignKey('usermessage.usename'))
    name=Column(String(20), nullable=False)
    branch=Column(String(20), nullable=False)
    nickname=Column(String(20), nullable=False)
    count= Column(Integer, default=0)
    place=Column(String(100), nullable=False)
    status = Column(String(20), nullable=False)

#定义用户信息表
class usermessage(Base):
    __tablename__='usermessage'
    usename = Column(String(20), primary_key=True)
    name=Column(String(20), nullable=False)
    branch=Column(String(20), nullable=False)
    password = Column(Integer, default=0)
    email=Column(String(20), nullable=False)
    tel=Column(Integer, default=0)
    address=Column(String(120), nullable=False)
    sex=Column(String(10), nullable=False)
    age=Column(Integer, default=0)

#用户激活信息表
class userregister(Base):
    __tablename__='userregister'
    usename = Column(String(20), primary_key=True)
    name=Column(String(20), nullable=False)
    branch=Column(String(20), nullable=False)
    password = Column(Integer, default=0)
    
Base.metadata.create_all(engine)
