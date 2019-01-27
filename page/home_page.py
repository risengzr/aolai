import page
from base.action import BaseAction


class HomePage(BaseAction):

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    # 点击首页我的按钮
    def click_my(self):
        self.click_element(page.aolai_home_btn_my)

