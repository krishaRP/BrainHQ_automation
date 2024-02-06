from selenium.webdriver.common.by import By
from commonLib import CommonLib
from time import sleep


## Class Authentication for brainhq authentication page
## ALL the variables are set for XPATH
## ALL functions are navigation function
class Authentication(CommonLib):
    FORM_LOGIN_PAGE_LOCATOR = (By.XPATH, '//*[@id="lola-neu-topbar-login"]')
    FORM_USERNAME = (By.XPATH, '//*[@id="login-in"]/input')
    FORM_PASSWORD = (By.XPATH, '//*[@id="password-in"]/input')
    FORM_SUBMIT_BTN = (By.XPATH, "/html/body/div[8]/div[12]/div/div/div[1]/div/div[3]/div[1]/div[3]/span")
    FORM_LOGIN_BUTTON_FUNCTION = (By.XPATH, '//*[@id="login-in"]/input')
    NAV_BAR = (By.XPATH, '//*[@id="nav-trn"]')
    NAV_DROP = (By.XPATH, '//*[@id="nav-r"]/i[2]')
    LOGOUT_BTN = (By.XPATH, '//*[@id="logout"]/div[1]/a')
    LOGOUT_BTN_CHECK = (By.XPATH, '//*[@id="lola-neu-topbar-login"]')
    SIGN_UP_BTN = (By.XPATH,'//*[@id="guil-signup"]/a/button')
    SIGN_UP_SUBMIT = (By.XPATH, '//*[@id="post-form"]/div[2]/div')

    def navigate_to_login_page(self):
        self.wait_for(self.FORM_LOGIN_PAGE_LOCATOR).click()

    def enter_login_username(self, username):
        self.wait_for(self.FORM_USERNAME).send_keys(username)

    def enter_login_password(self, password):
        self.find(self.FORM_PASSWORD).send_keys(password)

    def check_login_function(self):
        self.maximize()
        self.wait_for(self.FORM_LOGIN_BUTTON_FUNCTION)

    def click_login_button(self):
        self.maximize()
        login_element = self.find(self.FORM_SUBMIT_BTN)
        self.driver.execute_script("arguments[0].scrollIntoView();", login_element)
        login_element.click()

    def check_login_status(self):
        return self.wait_for(self.NAV_BAR)

    def click_logout_button(self):
        self.wait_for(self.NAV_DROP).click()
        sleep(5)
        self.wait_for(self.LOGOUT_BTN).click()

    def logout_check(self):
        self.wait_for(self.FORM_LOGIN_PAGE_LOCATOR)

    def navigate_to_sign_up_page(self, username, password, first_name, last_name ):
        self.maximize()
        sleep(3)
        self.wait_for(self.SIGN_UP_BTN).click()
        sleep(5)
        self.wait_for(self.FORM_USERNAME).send_keys(username)
        self.find(self.FORM_PASSWORD).send_keys(password)
        sleep(5)
        self.find(self.SIGN_UP_SUBMIT).click()
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="first_name-in"]/input').send_keys(first_name)
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="last_name-in"]/input').send_keys(last_name)
        sleep(2)
        self.driver.find_element(By.XPATH, '//*[@id="post-form"]/div[1]/div[2]').click()
        sleep(10)
