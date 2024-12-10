from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome import webdriver

class Login_admin_Page:

    # locating the elements on this page
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    btn_login_xpath = "//button[normalize-space()='Log in']"

    # declaring the constructor
    def __init__(self,driver):
        self.driver = driver

    # performing the action methods to enter the user mail
    def enter_username(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    # performing the action methods to enter the user password
    def enter_password(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    # performing the action methods to click on login button
    def click_login(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()



