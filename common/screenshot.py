# encoding = utf-8
import os
import time
from common.handle_yaml import handleYaml


class Screen(object):
    """
    在执行用例的过程中，如果发现异常就截图
    """

    def __init__(self, driver):
        self.driver = driver

    def __call__(self, func):
        def inner(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except:
                now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
                self.driver.get_screenshot_as_file("s%.png" % now_time)
                raise

        return inner()


def set_file_path(pic_dir_name):
    """
    设置截图文件的路径
    :param pic_dir_name: 保存图片的目录名称
    :return:
    """
    root_path = os.path.abspath('..')
    now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
    img_path = root_path + pic_dir_name + str(now_time) + ".png"
    return img_path


if __name__ == '__main__':

    path = "/Screenshots/"
    a = set_file_path(handleYaml.get_data("pic_dir_name"))
    print(a)

