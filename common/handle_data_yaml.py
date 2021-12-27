# coding = utf-8

import os
import yaml
from yaml import Loader


class HandleYaml:
    """
    操作yaml文件的工具类
    """

    def __init__(self, file_path):
        self.file_path = file_path
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


if __name__ == '__main__':
    file_path = os.path.join(os.path.abspath(".."), "data", "school_module.yaml")
    handYaml = HandleYaml(file_path)
    a = handYaml.get_data("school_manage")
    print(a)
    print(type(a))
