from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from tests.base_test import BaseTest
from pages.login_page import LoginPage
from utils.read_config import ConfigReader
from time import sleep
import allure
class TestLogin(BaseTest):
    @allure.story("Login Test")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login(ConfigReader.get_username(), ConfigReader.get_password())


