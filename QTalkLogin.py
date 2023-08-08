import time
from selenium import webdriver

dr = webdriver.ChromeOptions()
dr.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=dr)

driver.get("https://chat.qspiders.com/")
time.sleep(5)


class TestDemo:
    def enter_phoneNo(self):
        driver.find_element("xpath", "//input[@name='number']").send_keys('9606526314')

    def enter_pswd(self):
        driver.find_element("xpath", "//input[@name='password']").send_keys('#Yals1999')

    def Login(self):
        driver.find_element("xpath", "//button[@type='submit']").click()

t = TestDemo()
t.enter_phoneNo()
t.enter_pswd()
t.Login()