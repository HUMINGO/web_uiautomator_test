# coding = utf-8

import os
import unittest
from common.driver_common import DriverCommon
from common.handle_yaml import handleYaml
from common.log import logging
from common.screenshot import Screen, set_file_path
from common.util import sleep
from common.handle_data_yaml import HandleYaml

log_file_path = os.path.join(os.path.abspath(".."), "logs/mylog.txt")  # 日志文件的路径

# 获取页面定位元素
yaml_path = os.path.join(os.path.abspath(".."), "data", "user_module.yaml")
yaml_data = HandleYaml(yaml_path)


class User(unittest.TestCase):
    driver = DriverCommon("Chrome")

    @classmethod
    def setUpClass(cls) -> None:
        logging.info("------------开始测试学校模块----------------")
        cls.driver.open(handleYaml.get_data("url"))
        cls.driver.max_windows()
        sleep(5)
        cls.driver.send_key("id", "custom-validation_username", handleYaml.get_data("login")["username"])
        cls.driver.send_key("id", "custom-validation_password", handleYaml.get_data("login")["password"])
        cls.driver.single_click("xpath", "//*[@id='app']/div/div/div[2]/form/div[3]/div/div/div/button")
        cls.driver.get_screen(set_file_path(handleYaml.get_data("pic_dir_name")))  # 登录成功截图

    def test_51_userList(self):
        """
        用户列表
        :return:
        """
        self.driver.single_click("xpath", "//*[@id='app']/section/aside/div/ul/li[4]/div/span[2]")
        sleep(1)
        self.driver.single_click("xpath", "//*[@id='sub_menu_3_$$_user/userList-popup']/li/span")
        sleep(1)
        self.driver.get_screen(set_file_path(handleYaml.get_data("pic_dir_name")))
        sleep(2)
        # 在用户名输入框输入用户名搜索
        self.driver.input_search("xpath", yaml_data.get_data("user_list_page")["user_input"]["xpath"],
                                 yaml_data.get_data("data")["user_input"], "xpath",
                                 yaml_data.get_data("user_list_page")["search_button"]["xpath"])
        self.driver.get_screen(set_file_path(handleYaml.get_data("pic_dir_name")))
        self.driver.single_click("xpath", yaml_data.get_data("user_list_page")["reset_button"]["xpath"])   # 点击重置按钮
        sleep(2)
        self.driver.get_screen(set_file_path(handleYaml.get_data("pic_dir_name")))
        self.driver.single_click("xpath", yaml_data.get_data("user_list_page")["reset_button"]["xpath"])  # 点击重置按钮
        # 根据用户类型搜索
        self.driver.single_click("xpath", yaml_data.get_data("user_list_page")["user_type"]["xpath"])
        self.driver.single_click("xpath", yaml_data.get_data("user_list_page")["user_type"]["ordinary_user"]["xpath"])
        self.driver.single_click("xpath", yaml_data.get_data("user_list_page")["search_button"]["xpath"])
        # 查看详情
        self.driver.single_click("xpath", yaml_data.get_data("user_list_page")["check_detail"]["xpath"])
        sleep(2)
        self.driver.get_screen(set_file_path(handleYaml.get_data("pic_dir_name")))




    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        logging.info("--------------用户模块测试结束-----------------")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User)
    runner = unittest.TextTestRunner
    runner.run(suite)
