from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import aliased, outerjoin
from sqlalchemy.testing.pickleable import User

from db_init import Session, Department, Employee

# # Session默认开启事务
# with Session() as session: # 这里默认开始事务
#     dep = Department(name='oooo1')
#     session.add(dep)
#     session.commit()
#     # 如果产生任何异常，事务将自动rollback

# # 自动提交事务
# with Session() as session:
#     with session.begin():
#         dep = Department(name='oooo1')
#         session.add(dep)
#     # 这里如果没有异常则会自动提交事务
# # 这里会自动关闭session

# begin的另一种写法
with Session() as session, session.begin():
    dep = Department(name='aaa')
    session.add(dep)
# 这里如果没有异常则会自动提交事务
# 这里会自动关闭session

# # 多数据源事务处理
# # 同时开始和提交事务
# with Session(engine) as session1, session1.begin(), Session(engine2) as session2, session2.begin():
#     dep = Department(name='KKK')
#     session1.add(dep)
#
#     user = User(name='PPP')
#     session2.add(user)
