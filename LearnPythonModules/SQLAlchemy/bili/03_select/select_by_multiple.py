from db_init import engine, person_table
from sqlalchemy.sql import and_,or_

with engine.connect() as conn:
    # 创建查询对象,条件查询中c表示Column（列），
    # query = person_table.select().where(person_table.c.birthday > '2000-10-13').where(person_table.c.id < 6)
    # query = person_table.select().where(person_table.c.birthday > '2000-10-13').where(person_table.c.id < 6)
    query = person_table.select().where(
        or_(
            person_table.c.name == 'Tom',
            and_(
                person_table.c.birthday > '2000-10-13',
                person_table.c.id < 7
            )
        )
    )
    # 执行查询
    result_set = conn.execute(query)

    result = result_set.fetchall()
    print(result)
