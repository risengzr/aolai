import page
from base.action import BaseAction


class PersonCenterPage(BaseAction):

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    # 点击左上角设置按钮
    def click_setting(self):
        self.click_element(page.aolai_person_center_btn_left_setting)