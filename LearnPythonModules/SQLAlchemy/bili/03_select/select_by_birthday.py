from db_init import engine,person_table

with engine.connect() as conn:
    # 创建查询对象,条件查询中c表示Column（列），
    query = person_table.select().where(person_table.c.birthday > '2000-10-13')
    # 执行查询
    result_set = conn.execute(query)

    result = result_set.fetchall()
    print(result)