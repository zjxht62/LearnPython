from sqlalchemy.sql import and_

from db_init import Session, Person

# 实例化Session类
session = Session()


# 单条记录查询的返回
# 使用first()
# person = session.query(Person).filter(Person.address == 'aaa').first()
# person = session.query(Person).filter(Person.id == 100).first()

# 使用one(),结果集中有且仅有一条记录时才能调用one()
# person = session.query(Person).filter(Person.id < 100).one() # 报错
# person = session.query(Person).filter(Person.id == 1).one()

# 使用scalar()，如果没有记录，或者只有一条记录时使用
# person = session.query(Person).filter(Person.id == 100).scalar() # 不会报错
person = session.query(Person).filter(Person.id == 1).scalar()

if person:
    print(f'name:{person.name},birthday:{person.birthday}')
