import sqlalchemy

engine = sqlalchemy.create_engine('mysql://root:znrh%40123@192.168.1.240/testdb', echo=True)

meta_data = sqlalchemy.MetaData()

# 需要第二个参数传入meta_data对象,每个表的创建信息都存在meta_data中
person_table = sqlalchemy.Table(
    'person', meta_data,
    sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True),  # 默认自增
    sqlalchemy.Column('name', sqlalchemy.String(128), unique=True, nullable=False),
    sqlalchemy.Column('birthday', sqlalchemy.Date(), nullable=False),
    sqlalchemy.Column('address', sqlalchemy.String(255), nullable=True),

)
meta_data.create_all(engine)