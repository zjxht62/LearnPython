import pymysql


class DbHelper:
    def __init__(self):
        self.db = None

    def get_db_connection(self, host, user_name, password, db, port=3306):
        print('开始连接数据库，host：{}， 端口：{}，用户名：{}， 密码：{}，数据库名{}'.format(host, port, user_name, password, db))
        db = pymysql.connect(host=host, port=port, user=user_name, passwd=password, db=db)
        self.db = db

    def exec_select_sql(self, sql):
        """
        执行数据库查询
        :param app: 应用名
        :param sql: 执行的sql
        :return: 查询结果
        """
        db = self.db
        cursor = db.cursor()
        print('执行查询SQL: %s' % sql)
        cursor.execute(sql)
        data = cursor.fetchall()
        print('查出的结果', data)
        db.close()
        return data

    def exec_update(self, sql):
        """
        执行数据库更新
        :param app: 应用名
        :param sql: 执行的sql
        :return:
        """
        db = self.db
        cursor = db.cursor()
        try:
            # 执行SQL语句
            print('执行更新SQL: %s' % sql)
            cursor.execute(sql)
            # 提交到数据库执行
            db.commit()
            print('影响行数: %s' % cursor.rowcount)
        except:
            # 发生错误时回滚
            db.rollback()
        # 关闭数据库连接
        db.close()

    def exec_updates(self, sqls):
        db = self.db
        cursor = db.cursor()
        try:
            for sql in sqls:
                # 执行SQL语句
                print('执行更新SQL: %s' % sql)
                cursor.execute(sql)
                # 提交到数据库执行
                db.commit()
                print('影响行数: %s' % cursor.rowcount)
        except:
            # 发生错误时回滚
            db.rollback()
        # 关闭数据库连接
        db.close()


