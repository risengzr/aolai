import os, sys
sys.path.append(os.getcwd())
import page
import pytest
from base.read_yaml import read_data
from page.collect_page_obj import CollectPage
from base.driver import init_driver


def read_yaml_file():
    li = []
    data = read_data("login.yaml")
    for i in data.keys():
        username = data.get(i).get("username")
        password = data.get(i).get("password")
        tag = data.get(i).get("tag")
        expect_data = data.get(i).get("except_data")
        li.append((username, password, tag, expect_data))
    return li


class TestLogin:

    def setup_class(self):
        self.driver = init_driver()
        self.collect_page = CollectPage(self.driver)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.parametrize("username, password, tag, except_data", read_yaml_file())
    def test_login(self, username, password, tag, except_data):
        # 点击我的
        self.collect_page.home_page_obj().click_my()
        # 点击已有账号
        self.collect_page.regist_page_obj().click_btn_already_account()
        # 输入用户名密码
        self.collect_page.login_page_obj().click_login(username, password)

        if tag == 1:
            try:
                # 点击设置
                self.collect_page.person_page_obj().click_setting()
                # 实现滑动，点击退出，点击确定
                self.collect_page.setting_page_obj().click_setting_btn_logout()
            except Exception:
                # 6.当出现异常的情况 实现截图操作
                self.collect_page.setting_page_obj().screen()
        else:
            #7.获取到弹出toast内容 应该是预期结果和实际的结果做对比
            toast_msg = self.collect_page.setting_page_obj().find_element(page.aolai_toast_pwd_error).text

            #8.判断预期结果和实际结果是否一致，不是则截图
            assert toast_msg == except_data, self.collect_page.setting_page_obj().screen()

            #9.关闭当前登录页面
            self.collect_page.login_page_obj().click_close_login_page()