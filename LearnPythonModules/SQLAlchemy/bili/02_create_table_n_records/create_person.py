import sqlalchemy

engine = sqlalchemy.create_engine('mysql://root:znrh%40123@192.168.1.240/testdb', echo=True)

meta_data = sqlalchemy.MetaData()

# 需要第二个参数传入meta_data对象,每个表的创建信息都存在meta_data中
person = sqlalchemy.Table(
    'person', meta_data,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),  # 默认自增
    sqlalchemy.Column('name', sqlalchemy.String(128), unique=True, nullable=False),
    sqlalchemy.Column('birthday', sqlalchemy.Date(), nullable=False),

)
meta_data.create_all(engine)

## insert a record
# # Generate an _sql.Insert construct against this _expression.TableClause.
# person_insert = person.insert()
# print(person_insert)
# insert_tom = person_insert.values(name="TomTom", birthday='2000-10-11')
#
# with engine.connect() as conn:
#     result = conn.execute(insert_tom)
#     print(result.inserted_primary_key)
#     # sqlalchemy默认开启事务，需要手动提交
#     conn.commit()

## batch insert
person_insert = person.insert()
with engine.connect() as conn:
    conn.execute(person_insert,[
        {'name':'Jack','birthday':'2000-10-13'},
        {'name':'Mary','birthday':'2000-10-14'},
        {'name':'Simth','birthday':'2000-10-15'},
    ])
    conn.commit()