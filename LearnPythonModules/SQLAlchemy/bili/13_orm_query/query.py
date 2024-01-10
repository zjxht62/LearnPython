from sqlalchemy import select
from sqlalchemy.orm import aliased, outerjoin

from db_init import Session, Department, Employee


def execute_query(query):
    result = session.execute(query)
    for row in result:
        print(row)


# 查询单个类
def select_single_target():
    query = select(Department).order_by(Department.name)
    execute_query(query)


# 查询多个类
def select_multiple():
    # 关联查询多个类，在join时指定类中的关联属性
    # isouter定义使用外连接
    query = select(Employee, Department).join(Employee.department,isouter=True)
    # query = select(Employee, Department).join(Department.employees)
    execute_query(query)


def select_with_alias():
    emp_cls = aliased(Employee, name='emp')
    dep_cls = aliased(Department, name='dep')
    query = select(emp_cls, dep_cls).join(emp_cls.department.of_type(dep_cls))
    execute_query(query)

# 查询多个类中的个别字段
def select_fields():
    # 给字段起别名
    query = select(Employee.name.label('emp_name'), Department.name.label('dep_name')).join_from(Employee, Department)
    execute_query(query)

# OUTER JOIN
def select_fields_outer():
    # 外连接的两种写法
    query = select(Employee.name.label('emp_name'), Department.name.label('dep_name')).outerjoin_from(Employee, Department)
    # query = select(Employee.name.label('emp_name'), Department.name.label('dep_name')).select_from(outerjoin(Employee,Department))
    execute_query(query)

def where_object():
    dep = session.get(Department, 1)
    # query = select(Employee).where(Employee.department == dep)
    # query = select(Employee).where(Employee.dep_id == dep.id)
    query = select(Employee).where(Employee.dep_id != dep.id)
    execute_query(query)

def select_contains():
    emp = session.get(Employee, 1)
    query = select(Department).where(Department.employees.contains(emp))
    execute_query(query)


session = Session()
# select_single_target()
# select_multiple()
# select_with_alias()
# select_fields()
# select_fields_outer()
# where_object()
select_contains()