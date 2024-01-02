from sqlalchemy.sql import and_

from db_init import Session, Person

# 实例化Session类
session = Session()

# 查询所有
# result = session.query(Person).all()
# 条件查询
result = session.query(Person).filter(
    and_(
        Person.birthday > '2000-10-13',
        Person.address == 'aaa'
    )
)


for person in result:
    print(f'name:{person.name},birthday:{person.birthday}')

