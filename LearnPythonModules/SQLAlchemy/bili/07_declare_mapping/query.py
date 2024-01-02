from db_init import Session, Person

# 实例化Session类
session = Session()

# p = Person(name='Amy', birthday='2000-9-18', address='unknown')
# session.add(p)

ps = [
    Person(name='Bob', birthday='1993-1-14', address='XiAn'),
    Person(name='Lily', birthday='2002-5-2', address='ChangSha')

]
session.add_all(ps)

session.commit()
