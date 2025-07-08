from selenium import webdriver
from tests.base_test import BaseTest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage
from utils.read_config import ConfigReader
from pages.admin_page import AdminPage
class TestAdmin(BaseTest):
    def test_recruitment_page_functionality(self):
        login_page = LoginPage(self.driver)
        login_page.login(ConfigReader.get_username(), ConfigReader.get_password())

        admin_page = AdminPage(self.driver)
        admin_page.navigate_to_admin()

        # admin_page.add_user(ConfigReader.get_new_user())
        # admin_page.search_user(ConfigReader.get_new_user()["username"])