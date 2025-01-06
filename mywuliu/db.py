import pprint
import pymysql

# 封装一个方法， 返回一个和数据库的链接


def get_conn():
    return pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="wuliu1230",
        charset="utf8",
    )


# 封装一个查询方法
def query_data(sql):
    conn = get_conn()
    try:
        # 创建游标查询数据， 返回字典格式数据
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        # 执行sql语句
        cursor.execute(sql)
        # 返回查询结果
        return cursor.fetchall()
    finally:
        cursor.close()  # 关闭游标
        conn.close()  # 关闭链接


def insert_or_update_data(sql):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    # sql = """
    #     select * from users;
    # """
    #
    # data = query_data(sql)
    # pprint.pprint(data)

    sql = """
        update users set password="0000000"
        where id = 4
    """
    insert_or_update_data(sql)
