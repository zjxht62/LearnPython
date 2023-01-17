import pymysql.cursors

# 连接数据库
connection = pymysql.connect(host='192.168.50.53',
                             user='root',
                             password='c9r6e2h7',
                             database='learn',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.SSCursor)

with connection:
    print(connection.open)
    with connection.cursor() as cursor:
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection并不是自动提交的，所以需要调用commit()方法来提交变更
    connection.commit()

    with connection.cursor() as cursor:
        # 读取单行记录
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)


