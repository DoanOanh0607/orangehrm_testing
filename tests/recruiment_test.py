from selenium import webdriver
from tests.base_test import BaseTest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.recruitment_page import RecruitmentPage
from pages.login_page import LoginPage
from utils.read_config import ConfigReader
from time import sleep
class TestRecruit(BaseTest):
    def test_recruitment_page_functionality(self):
        login_page = LoginPage(self.driver)
        login_page.login(ConfigReader.get_username(), ConfigReader.get_password())

        recruitment_page = RecruitmentPage(self.driver)
        recruitment_page.navigate_to_vacancies()
        recruitment_page.create_vacancy()
        sleep(10)
        recruitment_page.save_vacancy()
        recruitment_page.edit_vacancy()
        # recruitment_page.cancel_edit_and_verify_return()
        # recruitment_page.search_and_verify_vacancy()
        # recruitment_page.logout()
