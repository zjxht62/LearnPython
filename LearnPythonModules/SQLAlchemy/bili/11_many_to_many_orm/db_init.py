import datetime
from typing import List

from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Table
# from sqlalchemy.ext.declarative import declarative_base  # 用于映射类的基类
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, declarative_base, relationship  # 用于映射类的基类
from typing_extensions import Annotated
from sqlalchemy.sql import func

engine = create_engine('mysql://root:znrh%40123@192.168.1.240/testdb', echo=True)
Base = declarative_base()

# 使用Annotated定义字段信息，定义重复使用的字段类型，通过抽象提高复用程度
int_pk = Annotated[int, mapped_column(primary_key=True)]
required_unique_name = Annotated[str, mapped_column(String(128), unique=True, nullable=False)]
required_string = Annotated[str, mapped_column(String(128), nullable=False)]
timestamp_not_null = Annotated[datetime.datetime, mapped_column(nullable=False)]

# 定义关联表
association_table = Table(
    'user_role',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('role_id', ForeignKey('roles.id'), primary_key=True)
)


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int_pk]
    name: Mapped[required_unique_name]
    password: Mapped[required_string]

    roles: Mapped[List['Role']] = relationship(secondary=association_table, back_populates='users', lazy=False)

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}'


class Role(Base):
    __tablename__ = 'roles'
    id: Mapped[int_pk]
    name: Mapped[required_unique_name]

    users: Mapped[List['User']] = relationship(secondary=association_table, back_populates='roles', lazy=False)

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}'


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
