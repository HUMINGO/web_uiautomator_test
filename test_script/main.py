# coding:utf-8
import os
import time
import unittest
from TestRunner import HTMLTestRunner

"""
    执行脚本的主入口文件
"""


def get_all_case():
    """
    获取到所有的用例
    :return:
    """
    scripts_dir = os.path.join(os.path.abspath(".."), "test_script")
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(scripts_dir, pattern="test*.py", top_level_dir=None)
    # 将测试用例添加到测试套件中
    for test_suit in discover:
        for test_case in test_suit:
            testcase.addTests(test_case)
    return testcase


if __name__ == "__main__":
    report_path =os.path.join(os.path.abspath(".."), "test_report", "report.html")
    f = open(report_path, 'wb')
    HTMLTestRunner(
        stream=f,
        verbosity=2,
        title='体测大师管理后台UI自动化测试',
        description='UI自动化测试报告结果'
    ).run(get_all_case())
    f.close()

