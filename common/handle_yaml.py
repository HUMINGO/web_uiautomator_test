# coding = utf-8
import os

import yaml

from yaml import Loader

# filepath = "../config.yaml"
current_path = os.path.dirname(__file__)



class HandleYaml:
    """
    操作yaml文件的工具类
    """
    # filepath = os.path.join(os.path.abspath('..'), "config.yaml")

    def __init__(self):
        self.file_path = os.path.abspath('..') + "/config.yaml"
        self.all_data = None
        stream = open(self.file_path, mode="r", encoding="utf-8")
        self.all_data = yaml.load(stream, Loader)

    def get_data(self, section):
        """
        从yaml文件中获取用例
        :param section: 数据域
        :return:
        """
        return self.all_data[section]


handleYaml = HandleYaml()

if __name__ == '__main__':
    a = handleYaml.get_data("login")
    print(a)