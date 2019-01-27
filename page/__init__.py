from selenium.webdriver.common.by import By

# 登录功能元素定位数据

# 1.homoe页面
# 1.1定位到我的
aolai_home_btn_my = By.ID, "com.yunmall.lc:id/tab_me"
aolai_home_btn_shopping_cart = By.ID, "com.yunmall.lc:id/tab_shopping_cart"

# 2.注册页面
# 2.1定位到已有账号 去登录
aolai_regist_btn_already_account = By.ID, "com.yunmall.lc:id/gotologon"

# 3.登录页面
# 3.1 定位到账号
aolai_login_edit_account = By.ID, "com.yunmall.lc:id/logon_account_textview"
# 3.2 定位到密码
aolai_login_edit_password = By.ID, "com.yunmall.lc:id/logon_password_textview"
# 3.3 定位到登录按钮
aolai_login_btn_login = By.ID, "com.yunmall.lc:id/logon_button"
# 3.4 定位到关闭当前登录页面按钮
aolai_login_btn_close_login= By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"

# 4.个人中心页面
# 4.1 定位到左上角设置按钮
aolai_person_center_btn_left_setting = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_layout"

# 5 设置页面
# 5.1 退出按钮
aolai_setting_btn_setting_logout = By.ID, "com.yunmall.lc:id/setting_logout"
# 5.2 定位到弹框的确定按钮
aolai_setting_btn_dialog_confirm = By.ID, "com.yunmall.lc:id/ymdialog_right_button"

# 定位toast
aolai_toast_pwd_error = By.XPATH, "//*[contains(@text,'密码错误')]"