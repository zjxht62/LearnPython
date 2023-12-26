from urllib.parse import quote
from sqlalchemy import create_engine,text
# echo,展示数据库执行了哪些操作
engine = create_engine("mysql://root:%s@192.168.1.240/testdb" % quote("znrh@123"), echo=True)
connection = engine.connect()

# 使用原始语句查询
query = text('select * from students')

result_set = connection.execute(query)
for row in result_set:
    print(row)

connection.close()
engine.dispose()