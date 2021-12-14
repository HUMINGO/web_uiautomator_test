# coding = utf-8

import os
import unittest
from common.driver_common import DriverCommon
from common.handle_yaml import handleYaml
from common.log import logging
from common.screenshot import Screen, set_file_path
from common.util import *

log_file_path = os.path.join(os.path.abspath(".."), "logs/mylog.txt")  # 日志文件的路径
file_path = os.path.join(os.path.abspath(".."), "Screenshots")


class School(unittest.TestCase):
    driver = DriverCommon("Chrome")

    @classmethod
    def setUpClass(cls) -> None:
        logging.info("------------开始测试学校模块----------------")
        open(log_file_path, "w").close()  # 清空日志文件
        del_file(file_path)

    def setUp(self) -> None:
        """
        每个用例执行前，先登录，然后将浏览器最大化
        :return:
        """
        self.driver.open(handleYaml.get_data("url"))
        self.driver.max_windows()
        sleep(5)
        self.driver.send_key("id", "custom-validation_username", handleYaml.get_data("login")["username"])
        self.driver.send_key("id", "custom-validation_password", handleYaml.get_data("login")["password"])
        self.driver.single_click("xpath", "//*[@id='app']/div/div/div[2]/form/div[3]/div/div/div/button")
        self.driver.get_screen(set_file_path(handleYaml.get_data("pic_dir_name")))
        sleep(3)

    def test_1_createSchool(self):
        """
        创建学校
        :return:
        """
        self.driver.single_click("xpath", "//*[@id='app']/section/aside/div/ul/li[3]/div/span[2]")
        sleep(2)
        self.driver.single_click("xpath", "//*[@id='sub_menu_2_$$_school/schoolList-popup']/li[1]")
        self.driver.single_click("xpath", "//*[@id='app']/section/section/main/div/div[1]/div/div[2]/button/a")
        self.driver.get_screen(set_file_path(handleYaml.get_data("pic_dir_name")))
        sleep(2)
        # 进入到创建学校页面
        try:
            self.driver.send_key("xpath", "//*[@id='name']", "希望中学")
            # self.driver.single_click("xpath", "//*[@id='app']/section/section/main/div/div/form/div[2]/div[2]/div["
            #                               "1]/div/div")
            # 选择中学
            # self.driver.single_click("xpath", "/html/body/div[12]/div/div/div/div[2]/div[1]/div/div/div[2]/div")
            self.driver.single_click("xpath", "//*[@id='address']")
            self.driver.single_click("xpath", "/html/body/div[14]/div/div/div/ul/li[1]")

        except Exception as e:
            logging.info("创建学校失败，原因是{}".format(e))

    def tearDown(self) -> None:
        self.driver.close()

    @classmethod
    def tearDownClass(cls) -> None:
        logging.info("--------------学校模块测试结束-----------------")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(School)
    runner = unittest.TextTestRunner
    runner.run(suite)
