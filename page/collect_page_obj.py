from page.home_page import HomePage
from page.login_page import LoginPage
from page.person_center_page import PersonCenterPage
from page.regist_page import RegistPage
from page.setting_page import SettingPage


class CollectPage:

    def __init__(self, driver):
        self.driver = driver

    def home_page_obj(self):
        return HomePage(self.driver)

    def login_page_obj(self):
        return LoginPage(self.driver)

    def person_page_obj(self):
        return PersonCenterPage(self.driver)

    def regist_page_obj(self):
        return RegistPage(self.driver)

    def setting_page_obj(self):
        return SettingPage(self.driver)




