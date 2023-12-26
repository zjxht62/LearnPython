from db_init import engine,person_table

with engine.connect() as conn:
    # 创建查询对象
    query = person_table.select()
    # 执行查询
    result_set = conn.execute(query)

    # 返回迭代器
    # for row in result_set:
    #     print(row[0])# row其实是一个元祖，[0]表示第0列
    #     print(row.name)

    # 直接获取所有
    # result = result_set.fetchall()
    # print(result)

    # 只获取第一条
    row = result_set.fetchone()
    print(row)