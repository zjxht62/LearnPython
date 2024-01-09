from db_init import Session, User, Role


def insert_records(session):
    role1 = Role(name='Admin')
    role2 = Role(name='Operator')

    user1 = User(name='Jack', password='111')
    user2 = User(name='Tom', password='111')
    user3 = User(name='Mary', password='111')

    user1.roles.append(role1)
    user1.roles.append(role2)
    user2.roles.append(role1)
    user3.roles.append(role2)

    session.add_all([user1, user2, user3])
    session.commit()


def select_user(s: Session):
    u = s.query(User).filter(User.id == 1).one()
    print(u)
    print(u.roles)


def select_role(s:Session):
    r = s.query(Role).filter(Role.id ==1).one()
    print(r)
    print(r.users)


session = Session()
# insert_records(session)
# select_user(session)
select_role(session)