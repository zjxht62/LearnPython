from db_init import Session, Employee, Computer


def insert(s):
    c1 = Computer(model="Dell", number='1111')
    c2 = Computer(model="Surface", number='2222')
    c3 = Computer(model="Macbook Pro", number='3333')

    e1 = Employee(name="Jack", computer=c1)
    e2 = Employee(name="Tom", computer=c2)
    e3 = Employee(name="Mary", computer=c3)

    s.add_all([e1, e2, e3])
    s.commit()


def select(s):
    e = s.query(Employee).filter(Employee.id == 1).one()
    if e:
        print(e)
        print(e.computer)

    c = s.query(Computer).filter(Computer.id == 2).one()
    if c:
        print(c)
        print(c.employee)


def update1(s):
    s.query(Employee).filter(Employee.id == 3).update({Employee.computer_id: None})
    s.commit()


def update2(s):
    c = s.query(Computer).filter(Computer.id == 3).one()
    e = s.query(Employee).filter(Employee.id == 3).one()
    if c and e:
        e.computer = c
        s.commit()


session = Session()
# insert(session)
# select(session)
# update1(session)
update2(session)
