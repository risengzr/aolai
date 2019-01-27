import page
from base.action import BaseAction


class RegistPage(BaseAction):

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    # 点击：已有账号，去登陆
    def click_btn_already_account(self):
        self.click_element(page.aolai_regist_btn_already_account)
