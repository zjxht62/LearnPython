import random
import time, datetime
from typing import List
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime, Integer
from sqlalchemy import func, text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import sessionmaker


class Base(DeclarativeBase):
    pass


class Department(Base):
    # 表名dept为部门信息表
    __tablename__ = "dept"
    # id: Mapped[int] - 这部分是类型注解。Mapped[int]是来自sqlalchemy的类型，int为类型参数
    id: Mapped[int] = mapped_column(primary_key=True)
    # name为部门名称字段
    name: Mapped[str] = mapped_column(String(100))
    # update_at字段表示更新时间，默认值为当前系统时间
    update_at: Mapped[DateTime] = mapped_column(DateTime(), default=datetime.datetime.now)
    # employees对应该指定部门下的员工信息列表，back_populates表示反向关联的表名为自身，
    # cascade指定为级联删除，即删除部门信息会一并删除部门下的员工信息
    employees: Mapped[List["Employee"]] = relationship(back_populates="dept", cascade="all, delete-orphan")

    # 字符串形式表示Department对象
    def __repr__(self) -> str:
        return f"Department(id={self.id!r}, name={self.name!r})"

class Employee(Base):
    # 表名employee为员工信息表
    __tablename__ = "employee"
    # id为主键
    id: Mapped[int] = mapped_column(primary_key=True)
    # name为员工姓名
    name: Mapped[str] = mapped_column(String(100))
    # age为员工年龄
    age: Mapped[int] = mapped_column(Integer)
    # sex为员工性别
    sex: Mapped[str] = mapped_column(String(10))
    # dept_id为外键，对应dept表的id字段
    dept_id: Mapped[int] = mapped_column(ForeignKey("dept.id"))
    # update_at字段表示更新时间，默认值为当前系统时间
    update_at: Mapped[DateTime] = mapped_column(DateTime(), default=datetime.datetime.now)
    # dept和Department中的employees必须成对出现，否则会报错，表示两个表之间的关系back_populates对应employees，而不是表名employee
    dept: Mapped["Department"] = relationship(back_populates="employees")

    # 字符串形式表示Department对象
    def __repr__(self) -> str:
        return f"Employee(id={self.id!r}, name={self.name!r}, dept_id={self.dept_id!r})"


# 连接数据库并建表，SQLAlchemy使用engine对象负责使用DBAPI来适配不同类型的数据库
# 创建engine对象
engine = create_engine("sqlite:///demo.db", echo=False)
# 建立表
Base.metadata.create_all(engine)

# 增删改查
# 增删改查需要事先创建Session对象，类似于数据库中的事务操作对象
Session = sessionmaker(bind=engine)
session = Session()

def insert_demo():
    """插入表数据示例
    """
    # 部门信息记录
    dept_1 = Department(name="研发部")
    if session.query(Department).filter_by(name="研发部").first() is None:
        session.add(dept_1)
    dept_2 = Department(name="营销部")
    if session.query(Department).filter_by(name="营销部").first() is None:
        session.add(dept_2)
    session.commit()
    # 员工信息记录
    employee_list = []
    empoyee_1 = Employee(name="张三", age=20, sex="男", dept_id=dept_1.id)
    if session.query(Employee).filter_by(name="张三").first() is None:
        employee_list.append(empoyee_1)
    empoyee_2 = Employee(name="张小丽", age=23, sex="女", dept_id=dept_2.id)
    if session.query(Employee).filter_by(name="张小丽").first() is None:
        employee_list.append(empoyee_2)
    empoyee_3 = Employee(name="黎明", age=30, sex="男", dept_id=dept_2.id)
    if session.query(Employee).filter_by(name="黎明").first() is None:
        employee_list.append(empoyee_3)
    session.add_all(employee_list)
    session.commit()

def query_demo():
    """查询数据示例
    """
    dept_1 = session.query(Department).filter_by(name="研发部").first()
    print(f"查询部门名称为:{dept_1.name}")
    print(f"该部门下的员工有：{dept_1.employees}, 数量为{len(dept_1.employees)}")

def update_demo():
    """更新数据示例
    """
    employees = session.query(Employee).all()
    for emp in employees:
        # 年龄增加1
        emp.age += 1
        emp.update_at = datetime.datetime.now()
    session.commit()

def delete_demo():
    """删除数据示例
    """
    dept_1 = session.query(Department).filter_by(name="研发部").first()
    # 该部门名下的员工记录也会被删除
    session.delete(dept_1)
    session.commit()

insert_demo()
query_demo()
update_demo()