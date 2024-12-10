import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.network import set_data_size_limits_for_test
from base_pages.Login_Admin_Page import Login_admin_Page
from utilities.read_properties import Read_Config
from utilities.custom_logger import Log_Maker


class Test_01_Admin_Login:

    # all the variables those are going to get used in this page
    admin_page_url = Read_Config.get_admin_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    logger = Log_Maker.log_gen()

    def test_title_verification(self,setup):
        self.logger.info("*************************Test Case 1 passed*************************")
        self.driver = setup
        self.driver.get(self.admin_page_url)
        time.sleep(5)
        act_title = self.driver.title
        exp_title = "Your store. Login"
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, "test_title_verification.png")

        self.driver.save_screenshot(screenshot_path)
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_valid_admin_login(self,setup):
        self.logger.info("************************Test Case 2 passed**************************")
        self.driver = setup
        self.driver.get(self.admin_page_url)

        # create the object of page class
        self.admin_lp = Login_admin_Page(self.driver)
        self.admin_lp.enter_username(self.username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, "test_valid_admin_login.png")

        self.driver.save_screenshot(screenshot_path)
        self.driver.close()

    def test_invalid_admin_login(self,setup):
        self.logger.info("************************Test Case 3 passed**************************")
        self.driver = setup
        self.driver.get(self.admin_page_url)

        # create the object of page class
        self.admin_lp = Login_admin_Page(self.driver)
        self.admin_lp.enter_username(self.invalid_username)
        self.admin_lp.enter_password(self.password)
        self.admin_lp.click_login()
        time.sleep(5)
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)
        screenshot_path = os.path.join(screenshot_dir, "test_invalid_admin_login.png")

        self.driver.save_screenshot(screenshot_path)
        self.driver.close()


