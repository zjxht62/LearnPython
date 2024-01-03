import datetime

from sqlalchemy import create_engine, Column, Integer, String, Date
# from sqlalchemy.ext.declarative import declarative_base  # 用于映射类的基类
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, declarative_base # 用于映射类的基类
from typing_extensions import Annotated
from sqlalchemy.sql import func

engine = create_engine('mysql://root:znrh%40123@192.168.1.240/testdb', echo=True)
Base = declarative_base()

# 使用Annotated定义字段信息，定义重复使用的字段类型，通过抽象提高复用程度
int_pk = Annotated[int, mapped_column(primary_key=True)]
required_unique_name = Annotated[str, mapped_column(String(128), unique=True, nullable=False)]
timestamp_default_now = Annotated[datetime.datetime, mapped_column(nullable=False, server_default=func.now())]

class Customer(Base):
    # 数据库中与类对应的表名
    __tablename__ = 'customers'

    # 使用Mapped泛型定义表中的列
    # 使用mapped_column指定更多信息
    # id: Mapped[int] = mapped_column(primary_key=True)
    # name: Mapped[str] = mapped_column(String(128), unique=True, nullable=False)

    # 直接使用定义好的类型
    id: Mapped[int_pk]
    name: Mapped[required_unique_name]
    birthday: Mapped[datetime.datetime]
    create_time:Mapped[timestamp_default_now]


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
