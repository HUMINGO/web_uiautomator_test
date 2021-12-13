# coding = utf-8
import os.path
import unittest
# from common.handle_yaml import *

case_path = os.path.join(os.getcwd(), "test_script")

report_path = os.path.join(os.getcwd(), "test_report")

discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)

print(discover)

runner = unittest.TextTestRunner()
runner.run(discover)

print(os.getcwd())
