from sqlalchemy.sql import and_

from db_init import Session, Customer

# 实例化Session类
session = Session()

c = Customer(name='Jack', birthday='2000-10-1')
session.add(c)
session.commit()
