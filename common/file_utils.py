# coding = utf-8
import os


def del_file(filepath):
    """
    删除某个目录下的所有文件
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path) or os.path.isdir(file_path):
            os.remove(file_path)


if __name__ == '__main__':
    file_path = os.path.join(os.path.abspath(".."), "Screenshots")
    print(file_path)
    del_file(file_path)