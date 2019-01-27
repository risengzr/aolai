import page
from base.action import BaseAction


class LoginPage(BaseAction):

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    # 输入账号密码，点击登录
    def click_login(self, username, password):
        self.send_element(page.aolai_login_edit_account, username)
        self.send_element(page.aolai_login_edit_password, password)
        self.click_element(page.aolai_login_btn_login)

    # 点击关闭登录页面按钮
    def click_close_login_page(self):
        self.click_element(page.aolai_login_btn_close_login)