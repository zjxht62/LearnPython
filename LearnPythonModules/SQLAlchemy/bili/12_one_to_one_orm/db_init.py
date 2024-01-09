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


class Employee(Base):
    __tablename__ = 'employee'
    id: Mapped[int_pk]
    name: Mapped[required_unique_name]
    computer_id: Mapped[int] = mapped_column(ForeignKey('computer.id'), nullable=True)

    # 以下两种方式效果相同
    # 1：使用类似注解的方式定义属性，指示该属性 computer 的类型为 Mapped['Computer']，这实际上是对 Computer 类型的引用。
    computer: Mapped['Computer'] = relationship(lazy=False, back_populates='employee')

    # 2：定义一个属性computer，关联到Computer模型
    # computer=relationship("Computer",lazy=False, back_populates='employee')

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}'


class Computer(Base):
    __tablename__ = 'computer'
    id: Mapped[int_pk]
    model: Mapped[required_string]
    number: Mapped[required_unique_name]

    employee: Mapped['Employee'] = relationship(lazy=False, back_populates='computer')

    def __repr__(self):
        return f'id: {self.id}, model: {self.model}, number: {self.number}'


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
