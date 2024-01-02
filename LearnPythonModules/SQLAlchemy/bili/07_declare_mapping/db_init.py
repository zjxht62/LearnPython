from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base  # 用于映射类的基类
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://root:znrh%40123@192.168.1.240/testdb', echo=True)
Base = declarative_base()


class Person(Base):
    # 数据库中与类对应的表名
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), unique=True, nullable=False)
    birthday = Column(Date, nullable=False)
    address = Column(String(255), nullable=True)


Base.metadata.create_all(engine)
# 使用session代替connection，
# 用sessionmaker创建一个Session类，之后在使用的时候实例化这个Session类
Session = sessionmaker(bind=engine)