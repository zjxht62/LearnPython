from db_init import Session, Department, Employee


def insert_employee(session):
    d1 = Department(name='hr')
    session.add(d1)

    e1 = Employee(dep_id=d1.id, name='Jack', birthday='2000-10-1')
    session.add(e1)

    session.commit()


session = Session()
insert_employee(session)
