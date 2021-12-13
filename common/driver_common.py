# coding = utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class DriverCommon:
    
    def __init__(self, browser):
        """
        初始化浏览器
        :param browser: 浏览器名称
        """
        if browser == 'firefox' or browser == 'Firefox' or browser == 'f' or browser == 'F':
            driver = webdriver.Firefox()
        elif browser == 'Ie' or browser == 'ie' or browser == 'i' or browser == 'I':
            driver = webdriver.Ie()
        elif browser == 'Chrome' or browser == 'chrome' or browser == 'Ch' or browser == 'ch':
            driver = webdriver.Chrome()
        elif browser == 'PhantomJS' or browser == 'phantomjs' or browser == 'ph' or browser == 'phjs':
            driver = webdriver.PhantomJS()
        elif browser == 'Edge' or browser == 'edge' or browser == 'Ed' or browser == 'ed':
            driver = webdriver.Edge()
        elif browser == 'Opera' or browser == 'opera' or browser == 'op' or browser == 'OP':
            driver = webdriver.Opera()
        elif browser == 'Safari' or browser == 'safari' or browser == 'sa' or browser == 'saf':
            driver = webdriver.Safari()
        else:
            raise NameError('只能输入firefox,Ie,Chrome,PhantomJS,Edge,Opera,Safari')
        self.driver = driver

    def get_element(self, fangfa, dingwei):
        """
        获得定位元素
        :param fangfa: 定位方式
        :param dingwei: 传入的定位值
        :return: 返回目标对象
        """
        if fangfa == 'id':
            element = self.driver.find_element_by_id(dingwei)
        elif fangfa == "name":
            element = self.driver.find_element_by_name(dingwei)
        elif fangfa == "class":
            element = self.driver.find_element_by_class_name(dingwei)
        elif fangfa == "link_text":
            element = self.driver.find_element_by_link_text(dingwei)
        elif fangfa == "xpath":
            element = self.driver.find_element_by_xpath(dingwei)
        elif fangfa == "tag":
            element = self.driver.find_element_by_tag_name(dingwei)
        elif fangfa == "css":
            element = self.driver.find_element_by_css_selector(dingwei)
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
        return element

    def get_elements(self, fangfa, dingwei):  # 组定位
        """
        组定位，获得一组定位对象
        :param fangfa: 定位方式
        :param dingwei: 传入的定位值
        :return:
        """
        if fangfa == 'id':
            element = self.driver.find_elements_by_id(dingwei)
        elif fangfa == "name":
            element = self.driver.find_elements_by_name(dingwei)
        elif fangfa == "class":
            element = self.driver.find_elements_by_class_name(dingwei)
        elif fangfa == "link_text":
            element = self.driver.find_elements_by_link_text(dingwei)
        elif fangfa == "xpath":
            element = self.driver.find_elements_by_xpath(dingwei)
        elif fangfa == "tag":
            element = self.driver.find_elements_by_tag_name(dingwei)
        elif fangfa == "css":
            element = self.driver.find_elements_by_css_selector(dingwei)
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css','tag'.")
        return element

    def wait_element_appear(self, fangfa, dingwei, wait=6):  # 等待
        """
        等待一个元素出现
        :param fangfa: 定位方式
        :param dingwei: 传入的定位值
        :param wait:
        :return:
        """
        if fangfa == "id":
            WebDriverWait(self.driver, wait, 1).until(EC.presence_of_element_located((By.ID, dingwei)))
        elif fangfa == "name":
            WebDriverWait(self.driver, wait, 1).until(EC.presence_of_element_located((By.NAME, dingwei)))
        elif fangfa == "class":
            WebDriverWait(self.driver, wait, 1).until(EC.presence_of_element_located((By.CLASS_NAME, dingwei)))
        elif fangfa == "link_text":
            WebDriverWait(self.driver, wait, 1).until(EC.presence_of_element_located((By.LINK_TEXT, dingwei)))
        elif fangfa == "xpath":
            WebDriverWait(self.driver, wait, 1).until(EC.presence_of_element_located((By.XPATH, dingwei)))
        elif fangfa == "css":
            WebDriverWait(self.driver, wait, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, dingwei)))
        else:
            raise NameError("Please enter the  elements,'id','name','class','link_text','xpath','css'.")

    def open(self, url):
        """
        打开网页
        :param url:地址
        :return:
        """
        self.driver.get(url)

    def max_windows(self):
        """
        最大化浏览器
        :return:
        """
        self.driver.maximize_window()

    def set_windows_size(self, wide, height):
        """
        设置窗口大小
        :param wide: 宽度
        :param height: 高度
        :return:
        """
        self.driver.set_window_size(wide, height)

    def send_key(self, fangfa, dingwei, text):
        """
        发送内容
        1、找到元素
        2、清空输入框
        3、输入数据
        :param fangfa: 定位方式
        :param dingwei: 传入的定位值
        :param text: 输入的文本
        :return:
        """
        self.wait_element_appear(fangfa, dingwei)
        e1 = self.get_element(fangfa, dingwei)
        e1.clear()
        e1.send_keys(text)

    def clear(self, fangfa, dingwei):
        """
        清空输入框中的值
        1、等待元素出现
        2、获取元素，清空输入框中的值
        :param fangfa: 定位方式
        :param dingwei: 传入的定位值
        :return:
        """
        self.wait_element_appear(fangfa, dingwei)
        e1 = self.get_element(fangfa, dingwei)
        e1.clear()

    def single_click(self, fangfa, dingwei):
        """
        等待一个元素出现后然后单击
        :param fangfa: 定位方式
        :param dingwei: 传入的定位值
        :return:
        """
        self.wait_element_appear(fangfa, dingwei)
        e1 = self.get_element(fangfa, dingwei)
        e1.click()

    def right_click(self, fangfa, dingwei):
        """
        等待一个元素出现后然后右击
        :param fangfa: 定位方式
        :param dingwei: 传入的定位值
        :return:
        """
        self.wait_element_appear(fangfa, dingwei)
        e1 = self.get_element(fangfa, dingwei)
        ActionChains(self.driver).context_click(e1).perform()

    def move_element(self, fangfa, dingwei):
        """
        将鼠标移动到元素中间
        :param fangfa: 定位方式
        :param dingwei: 传入的定位值
        :return:
        """
        self.wait_element_appear(fangfa, dingwei)
        e1 = self.get_element(fangfa, dingwei)
        ActionChains(self.driver).move_to_element(e1).perform()

    def double_click(self, dingwei, fangfa):
        """
        等待元素出现后双击
        :param dingwei: 定位方式
        :param fangfa: 传入的定位值
        :return:
        """
        self.wait_element_appear(fangfa, dingwei)
        e1 = self.get_element(fangfa, dingwei)
        ActionChains(self.driver).double_click(e1).perform()

    def drag_and_drop(self, fangfa1, e1, fangfa2, e2):
        """
        将一个元素移动到另一个元素所在的位置
        :param fangfa1: 定位方式 1
        :param e1: 元素 1
        :param fangfa2: 定位方式 2
        :param e2: 元素 2
        :return:
        """
        self.wait_element_appear(fangfa1, e1)
        ele1 = self.get_element(fangfa1, e1)
        self.wait_element_appear(fangfa2, e2)
        ele2 = self.element(fangfa2, e2)
        ActionChains(self.driver).drag_and_drop(ele1, ele2).perform()

    def click_text(self, text):
        """
        点击文字
        :param text: 文本
        :return:
        """
        self.driver.find_element_by_link_text(text).click()

    def close(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.close()

    def kill(self):
        """
        退出
        :return:
        """
        self.driver.quit()

    def submits(self, fangfa, dingwei):
        """
        提交
        :param fangfa: 定位方式
        :param dingwei: 传入的定位值
        :return:
        """
        self.wait_element_appear(fangfa, dingwei)
        e1 = self.get_element(fangfa, dingwei)
        e1.submit()

    def f5(self):
        """
        刷新
        :return:
        """
        self.driver.refresh()

    def js(self, sprit):
        """
        执行js脚本
        :param sprit: js 脚本
        :return:
        """
        self.driver.execute_script(sprit)

    def get_attribute(self, fangfa, dingwei, attribute_name):
        """
        获取元素的属性值
        :param attribute_name: 属性名
        :param fangfa: 定位方式
        :param dingwei: 传入的定位值
        :return:
        """
        e1 = self.get_element(fangfa, dingwei)
        return e1.get_attribute(attribute_name)

    def get_text(self, fangfa, dingwei):
        """
        获取一个元素的文本数据
        :param fangfa: 定位方式
        :param dingwei: 传入的定位值
        :return:
        """
        self.wait_element_appear(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        return e1.text

    def element_is_display(self, fangfa, dingwei):
        """
        获取到的元素是否可见
        :param fangfa: 定位方式
        :param dingwei: 传入的定位值
        :return:
        """
        self.wait_element_appear(fangfa, dingwei)
        e1 = self.element(fangfa, dingwei)
        return e1.is_displayed()

    def get_title(self):
        """
        # 获取title
        :param fangfa: 定位方式
        :param dingwei: 传入的定位值
        :return:
        """
        return self.driver.title

    def get_screen(self, file_path):
        """
        截屏
        :param file_path: 将截图存放的路径
        :return:
        """
        self.driver.get_screenshot_as_file(file_path)

    def implicitly_wait(self, fangfa, dingwei):
        """
        # 隐式等待
        :param fangfa: 定位方式
        :param dingwei: 传入的定位值
        :return:
        """
        self.driver.implicitly_wait((fangfa, dingwei))

    def accpet_alert(self):
        """
        # 允许 alert
        :return:
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        不允许alert
        :return:
        """
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, fangfa, dingwei):
        """
        # 切换 iframe
        :param fangfa: 定位方式
        :param dingwei: 传入的定位值
        :return:
        """
        self.wait_element_appear(fangfa, dingwei)
        if1 = self.element(fangfa, dingwei)
        self.driver.switch_to.frame(if1)
