import time


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, tp):
        time.sleep(1)
        return self.driver.find_element(tp[0], tp[1])

    def find_elements(self, tp):
        return self.driver.find_elements(tp[0], tp[1])

    def click_element(self, tp):
        self.find_element(tp).click()

    def send_element(self, tp, content):
        self.find_element(tp).send_keys(content)

    def slide_element(self, tag):
        time.sleep(1)
        # 获取当前手机窗口的大小
        screen_size = self.driver.get_window_size()
        width = screen_size.get("width")  # 获取手机宽
        height = screen_size.get("height")  # 获取手机的高
        if tag == 1:  # 向上滚动
            self.driver.swipe(width * 0.5, height * 0.8, width * 0.5, height * 0.3, 1000)
        if tag == 2:  # 向下滚动
            self.driver.swipe(width * 0.5, height * 0.3, width * 0.5, height * 0.8, 1000)
        if tag == 3:  # 向左滚动
            self.driver.swipe(width * 0.8, height * 0.5, width * 0.3, height * 0.5, 1000)
        if tag == 4:  # 向右滚动
            self.driver.swipe(width * 0.3, height * 0.5, width * 0.8, height * 0.5, 1000)

    def screen(self):
        png_name = "./screen/{}.png".format(int(time.time()))  # 截图名称
        self.driver.get_screenshot_as_file(png_name)



