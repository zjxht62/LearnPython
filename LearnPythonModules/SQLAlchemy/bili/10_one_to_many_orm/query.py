from db_init import Session, Department, Employee


def insert_employee(session):
    # 方案1：插入部门记录后，执行flush，获取到id，之后再插入员工信息
    # d1 = Department(name='hr')
    # session.add(d1)
    # 通过flush，将add操作提交
    # 但是这不是好的解决方案
    # session.flush()
    # e1 = Employee(dep_id=d1.id, name='Jack', birthday='2000-10-1')
    # session.add(e1)

    # 方案2：定义关联表对象
    d1 = Department(name='hr')
    e1 = Employee(department=d1, name='Jack', birthday="2000-10-1")
    session.add(e1)

    session.commit()


def select_employee(session):
    emp = session.query(Employee).filter(Employee.id == 1).one()

    print(emp)
    print(emp.department)

def select_department(session):
    dep = session.query(Department).filter(Department.id == 1).one()

    print(dep)
    print(dep.employees)

session = Session()
# insert_employee(session)
# select_employee(session)
select_department(session)