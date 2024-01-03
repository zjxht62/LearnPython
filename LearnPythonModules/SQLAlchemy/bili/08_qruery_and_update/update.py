from sqlalchemy.sql import and_

from db_init import Session, Person

# 实例化Session类
session = Session()

# 直接通过修改映射类的属性值来实现更新
# person = session.query(Person).filter(Person.id == 1).one()
# person.address = 'wwww'

# 先查询再update
# session.query(Person).filter(Person.id == 1).update({
#     Person.address:'PPPP',
#     Person.name:'Jerry'
# })

# 批量修改
session.query(Person).filter(Person.id > 6).update({
    Person.address:'Beijing',
})
session.commit()