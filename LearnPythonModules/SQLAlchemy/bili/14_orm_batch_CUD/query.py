from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import aliased, outerjoin

from db_init import Session, Department, Employee


def batch_insert():
    with Session() as session:
        session.execute(
            insert(Department).values(
                [
                    {'name': 'QA'},
                    {'name': 'R&D'},
                ]
            )
        )
        session.commit()


def batch_orm_insert():
    with Session() as session:
        session.execute(
            insert(Employee).values(
                [
                    {'dep_id': select(Department.id).where(Department.name == 'IT'),
                     'name': 'AAA',
                     'birthday': '1970-01-01', },
                    {'dep_id': select(Department.id).where(Department.name == 'HR'),
                     'name': 'BBB',
                     'birthday': '1970-01-02', },
                ]
            )
        )
        session.commit()


def batch_update():
    with Session() as session:
        session.execute(
            update(Employee),
            [
                {'id': 1, 'name': 'Jack111'},
                {'id': 2, 'birthday': '1970-01-01', },
            ]

        )
        session.commit()


def batch_delete():
    with Session() as session:
        session.execute(
            delete(Employee).where(Employee.name.in_(['AAA', 'BBB']))
        )
        session.commit()


# batch_insert()
# batch_orm_insert()
# batch_update()
batch_delete()