# coding = utf-8

import os
import unittest
from common.driver_common import DriverCommon
from common.handle_data_yaml import HandleYaml
from common.handle_yaml import handleYaml
from common.log import logging
from common.screenshot import Screen, set_file_path
from common.util import sleep
from common.file_utils import del_file

log_file_path = os.path.join(os.path.abspath(".."), "logs/mylog.txt")  # 日志文件的路径
file_path = os.path.join(os.path.abspath(".."), "Screenshots")
yaml_path = os.path.join(os.path.abspath(".."), "data", "school_module.yaml")
yaml_data = HandleYaml(yaml_path)


class School(unittest.TestCase):
    driver = DriverCommon("Chrome")

    @classmethod
    def setUpClass(cls) -> None:
        logging.info("------------开始测试学校模块----------------")
        open(log_file_path, "w").close()  # 清空日志文件
        # 删除所有的截图
        del_file(file_path)
        cls.driver.open(handleYaml.get_data("url"))
        cls.driver.max_windows()
        sleep(5)
        cls.driver.send_key("id", "custom-validation_username", handleYaml.get_data("login")["username"])
        cls.driver.send_key("id", "custom-validation_password", handleYaml.get_data("login")["password"])
        cls.driver.single_click("xpath", "//*[@id='app']/div/div/div[2]/form/div[3]/div/div/div/button")
        cls.driver.get_screen(set_file_path(handleYaml.get_data("pic_dir_name")))  # 登录成功截图

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

    def test_2_searchSchool(self):
        """
        搜索学校
        :return:
        """
        try:
            self.driver.single_click("xpath", yaml_data.get_data("school_manage")["xpath"])
            self.driver.single_click("xpath", yaml_data.get_data("school_manage")["sidebar"]["school_list"]["xpath"])
            sleep(2)
            self.driver.get_screen(set_file_path(handleYaml.get_data("pic_dir_name")))  # 截图
            self.driver.input_search("id",
                                     yaml_data.get_data("school_manage")["school_list"]["first_page"][
                                         "input_school_name"][
                                         "id"], "壹体研究院", "xpath",
                                     yaml_data.get_data("school_manage")["school_list"]["first_page"]["search_button"][
                                         "xpath"])
            # 点击重置按钮
            self.driver.single_click("xpath",
                                     yaml_data.get_data("school_manage")["school_list"]["first_page"]["reset_button"][
                                         "xpath"])
            # 点击学校下拉框
            self.driver.single_click("xpath",
                                     yaml_data.get_data("school_manage")["school_list"]["first_page"]["select_box"][
                                         "xpath"])
            # 选择小学
            self.driver.single_click("xpath",
                                     yaml_data.get_data("school_manage")["school_list"]["first_page"]["select_box"][
                                         "primary_school"]["xpath"])
            self.driver.single_click("xpath",
                                     yaml_data.get_data("school_manage")["school_list"]["first_page"]["search_button"][
                                         "xpath"])
            self.driver.get_screen(set_file_path(handleYaml.get_data("pic_dir_name")))  # 截图
        except Exception as e:
            logging.info("搜索学校失败，原因是{}".format(e))
            self.driver.get_screen(set_file_path(handleYaml.get_data("pic_dir_name")))
            sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        logging.info("--------------学校模块测试结束-----------------")


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(School)
    runner = unittest.TextTestRunner
    runner.run(suite)
