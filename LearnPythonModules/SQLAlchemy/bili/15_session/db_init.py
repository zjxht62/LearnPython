import datetime
from typing import List

from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base  # 用于映射类的基类
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, declarative_base, relationship  # 用于映射类的基类
from typing_extensions import Annotated
from sqlalchemy.sql import func

engine = create_engine('mysql://root:znrh%40123@192.168.1.240/testdb', echo=True)
Base = declarative_base()

# 使用Annotated定义字段信息，定义重复使用的字段类型，通过抽象提高复用程度
int_pk = Annotated[int, mapped_column(primary_key=True)]
required_unique_name = Annotated[str, mapped_column(String(128), unique=True, nullable=False)]
timestamp_not_null = Annotated[datetime.datetime, mapped_column(nullable=False)]


class Department(Base):
    __tablename__ = 'department'

    id: Mapped[int_pk]
    name: Mapped[required_unique_name]

    employees: Mapped[List["Employee"]] = relationship(back_populates="department")

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}'


class Employee(Base):
    __tablename__ = 'employee'

    id: Mapped[int_pk]
    dep_id: Mapped[int] = mapped_column(ForeignKey('department.id'))
    name: Mapped[required_unique_name]
    birthday: Mapped[timestamp_not_null]

    department: Mapped['Department'] = relationship(back_populates='employees')

    def __repr__(self):
        return f'id: {self.id}, dep_id: {self.dep_id}, name: {self.name}, birthday: {self.birthday}'


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
