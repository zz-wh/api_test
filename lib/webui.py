from selenium import webdriver

def open_browser():

    print('打开浏览器')
    wd = webdriver.Chrome(r'd:\web\chromedriver.exe')
    wd.implicitly_wait(5)

    return wd

# 登录
def mgr_login(wd):
    wd.get('http://10.67.48.35/kis/login')
    # 根据 ID 选择元素，并且输入字符串
    wd.find_element_by_id('username').send_keys('admin520')
    wd.find_element_by_id('password').send_keys('kedacom123.')
    # 根据标签名查找元素
    wd.find_element_by_id('loginBtn').click()

#登出
def mgr_logout(wd):
