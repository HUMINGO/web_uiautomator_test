# coding = utf-8
import os

import pymysql as pymysql
from common.handle_yaml import handleYaml


class HandleMysql:
    """
        1、数据库操作，查询数据库的数据
    """

    @staticmethod
    def connect_mysql():
        """
        连接数据库
        :return: 返回连接对象
        """
        data = handleYaml.get_data("mysql")
        host = data["host"]
        user = data["user"]
        password = data["password"]
        db = data["db"]
        charset = data["charset"]
        conn = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset)
        return conn

    @staticmethod
    def search(sql):
        """
        执行sql查询语句
        :param sql: 要执行的sql语句
        :return:
        """
        count = 0
        conn = HandleMysql.connect_mysql()
        cursor = conn.cursor()
        cursor.execute(sql)
        for i in cursor.fetchall():
            print(i)
        cursor.close()
        conn.close()

    @staticmethod
    def get_data(sql):
        """
        获取一条数据
        """
        conn = HandleMysql.connect_mysql()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return data

    @staticmethod
    def get_all_data(sql):
        """
        获取所有的数据，返回一个数据集合
        """
        all_data = []
        conn = HandleMysql.connect_mysql()
        cursor = conn.cursor()
        cursor.execute(sql)
        datas = cursor.fetchall()
        for data in datas:
            all_data.append(data[0])
        cursor.close()
        conn.close()
        return all_data


if __name__ == "__main__":
    sql = "select * from user limit 10"
    a = HandleMysql.get_all_data(sql)
    print(a)
