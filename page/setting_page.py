import page
from base.action import BaseAction


class SettingPage(BaseAction):

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    # 退出登录，滑动到最低端，点击退出，点击弹出框确定按钮
    def click_setting_btn_logout(self):
        self.slide_element(1)
        self.click_element(page.aolai_setting_btn_setting_logout)
        self.click_element(page.aolai_setting_btn_dialog_confirm)