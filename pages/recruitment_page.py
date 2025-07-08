from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.read_config import ConfigReader
from time import sleep
from datetime import datetime


class RecruitmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, ConfigReader.get_timeout())

        # Locators
        self.recruiment_menu = (By.XPATH, "//span[text()='Recruitment']")
        self.vacancy_tab = (By.XPATH, "//a[text()='Vacancies']")
        self.add_btn = (By.XPATH, "//button[normalize-space()='Add']")
        self.save_btn = (By.XPATH, "//button[normalize-space()='Save']")
        self.cancel_btn = (By.XPATH, "//button[normalize-space()='Cancel']")
        self.edit_title = (By.XPATH, "//h6[text()='Edit Vacancy']")
        self.vacancies_title = (By.XPATH, "//h5[text()='Vacancies']")
        self.add_title = (By.XPATH, "//h6[text()='Add Vacancy']")

    def navigate_to_vacancies(self):
        self.wait.until(EC.element_to_be_clickable(self.recruiment_menu)).click()
        self.wait.until(EC.element_to_be_clickable(self.vacancy_tab)).click()
        self.wait.until(EC.element_to_be_clickable(self.add_btn)).click()

    def create_vacancy(self):
        driver = self.driver
        current_date = datetime.now().strftime("%Y-%m-%d")
        vacancy = ConfigReader.get_vacancy()
        self.vacancy_name = f"{vacancy['vacancy_name']} {current_date}"

        self.wait.until(EC.visibility_of_element_located(self.add_title))
        driver.find_element(By.XPATH, "//label[text()='Vacancy Name']/following::input[1]").send_keys(self.vacancy_name)

        job_title_dropdown = driver.find_element(By.XPATH,"//label[text()='Job Title']/ancestor::div[contains(@class,'oxd-input-group')]/following-sibling::div//div[contains(@class,'oxd-select-text-input')]")
        job_title_dropdown.click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[@role='option']//span[text()='{vacancy['job_title']}']"))).click()

        driver.find_element(By.XPATH, "//label[text()='Description']/following::textarea[1]").send_keys(vacancy['description'])

    

        # hiring_input = driver.find_element(By.XPATH, "//label[text()='Hiring Manager']/following::input[1]")
        # hiring_input.clear()
        # hiring_input.send_keys(vacancy['hiring_manager'])


        driver.find_element(By.XPATH, "//label[text()='Number of Positions']/following::input[1]").send_keys(str(vacancy['number_of_position']))

        active_toggle = driver.find_element(By.XPATH, "//p[text()='Active']/following::div[1]//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
        if active_toggle.is_selected() != vacancy['active']:
            active_toggle.click()

        publish_rss = driver.find_element(By.XPATH, "//p[text()='Publish in RSS Feed and Web Page']/following::div[1]//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
        if not publish_rss.is_selected() != vacancy['publish_in_RSS_Feb_and_Web_page']:
            publish_rss.click()
        sleep(10)

    def save_vacancy(self):
        self.wait.until(EC.element_to_be_clickable(self.save_btn)).click()

    def edit_vacancy(self):
        edit_element = self.wait.until(EC.visibility_of_element_located(self.edit_title))
        assert edit_element.is_displayed(), "Trang Edit Vacancy không hiển thị"
        return edit_element

    def cancel_edit_and_verify_return(self):
        self.wait.until(EC.element_to_be_clickable(self.cancel_btn)).click()
        title = self.wait.until(EC.visibility_of_element_located(self.vacancies_title))
        assert title.is_displayed(), "Không quay lại trang Vacancies sau khi Cancel"

    def search_and_verify_vacancy(self, hiring_manager_full_name):
        driver = self.driver
        vacancy = ConfigReader.get_vacancy()

        job_title_filter = driver.find_element(
            By.XPATH,
            "//label[text()='Job Title']/ancestor::div[contains(@class,'oxd-input-group')]/following-sibling::div//div[contains(@class,'oxd-select-text-input')]"
        )
        job_title_filter.click()
        self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, f"//div[@role='option']//span[text()='{vacancy['job_title']}']"))
        ).click()

        hiring_input = driver.find_element(By.XPATH, "//label[text()='Hiring Manager']/following::input[1]")
        hiring_input.clear()
        hiring_input.send_keys(hiring_manager_full_name)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//span[text()='{hiring_manager_full_name}']"))).click()

        driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()

        rows = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='rowgroup']/div[@role='row']")))
        assert len(rows) > 0, "Không có vacancy nào được tìm thấy."

        matched = any(
            vacancy['vacancy_name_prefix'] in row.text and
            vacancy['job_title'] in row.text and
            hiring_manager_full_name in row.text
            for row in rows
        )
        assert matched, "Không tìm thấy vacancy với dữ liệu đúng."

    def logout(self):
        profile_menu = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-userdropdown-name")))
        profile_menu.click()
        logout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']")))
        logout_button.click()





        # Enter information for the form
        # self.vacancyname_input = (By.XPATH, "//label[text()='Vacancy Name']/following::input[1]")
        # self.job_title_dropdown = (By.XPATH, "//div[@class='oxd-select-text-input' and contains(text(), 'Select')]")
        # self.description = (By.XPATH, "//textarea[@placeholder='Type description here']")
        # self.hiring_manager_full_name = driver.find_element(By.XPATH, "//label[text()='Hiring Manager']/ancestor::div[contains(@class,'oxd-input-group')]//input[1]").get_attribute("value")
        # self.num_positions = (By.XPATH, "//label[text()='Number of Positions']/following::input[1]")
        # self.active_toggle = (By.XPATH, "//p[text()='Active']/following::div[1]//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
        # self.publish_rss = (By.XPATH, "//p[text()='Publish in RSS Feed and Web Page']/following::div[1]//span[@class='oxd-switch-input oxd-switch-input--active --label-right']")
        # self.save_btn = (By.XPATH, "//button[@type='submit']")
        # self.edit_title = (By.XPATH, "//h6[text()='Edit Vacancy']")
        # self.cancel_btn = (By.XPATH, "//button[normalize-space()='Cancel']")
        # self.vacancies_title = (By.XPATH, "//h5[text()='Vacancies']")
        # self.add_title = (By.XPATH, "//h6[text()='Add Vacancy']")
        
        
        # Edit Vacancy Page
        # self.edit_vacancy_page = (By.XPATH, "//h6[text()='Edit Vacancy']")
        # self.cancel_btn = (By.XPATH, "//button[text()=' Cancel ']")

        # Vacancies Page
        # self.vacancies_page = (By.XPATH, "//h5[text()='Vacancies']")
        
        # Search Vacancy
        # self.search_job_title = (By.XPATH, "//label[text()='Job Title']/ancestor::div[contains(@class,'oxd-input-group')]/following-sibling::div//div[contains(@class,'oxd-select-text-input')]")
        # self.search_hiring_manager = (By.XPATH, "//label[text()='Hiring Manager']/ancestor::div[contains(@class,'oxd-input-group')]/following-sibling::div//div[contains(@class,'oxd-select-text-input')]")
        # self.search_btn = (By.XPATH, "//button[@type='submit']")
    #     self.vacancy_table = (By.XPATH, "//div[@class='oxd-table-body']")
    #     self.vacancy_name_cell = (By.XPATH, "//div[@class='oxd-table-body']//div[contains(text(), '{}')]")
    #     self.job_title_cell = (By.XPATH, "//div[@class='oxd-table-body']//div[contains(text(), '{}')]")
    #     self.hiring_manager_cell = (By.XPATH, "//div[@class='oxd-table-body']//div[contains(text(), '{}')]")
    
    # def navigate_to_vacancies(self):
    #     self.wait.until(EC.element_to_be_clickable(self.recruiment_menu)).click()
    #     self.wait.until(EC.element_to_be_clickable(self.vacancy_tab)).click()
    #     self.wait.until(EC.element_to_be_clickable(self.add_btn)).click()
        
    # def create_vacancy(self):
    #     current_date = datetime.now().strftime("%Y-%m-%d")
    #     vacancy = ConfigReader.get_vacancy()
    #     # Enter Vacancy Name
    #     self.vacancy_name = f"{vacancy['vacancy_name']} {current_date}"
    #     self.wait.until(EC.element_to_be_clickable(self.vacancyname_input)).send_keys(self.vacancy_name)
    #     # Enter Job Title
    #     self.wait.until(EC.element_to_be_clickable(self.job_title_dropdown)).click()
    #     self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[@role='listbox']//span[text()='{vacancy['job_title']}']"))).click()
    #     # Enter Description
    #     self.wait.until(EC.element_to_be_clickable(self.description)).send_keys(vacancy['description'])

    #     # Enter Hiring Manager
    #     hiring_input = self.driver.find_element(By.XPATH, "//label[text()='Hiring Manager']/following::input[1]")
    #     hiring_input.send_keys(hiring_manager_full_name)
    #     self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//span[text()='{hiring_manager_full_name}']"))).click()



        # Enter Number of Positions
    #     self.wait.until(EC.element_to_be_clickable(self.num_positions)).send_keys(vacancy['number_of_position'])
    #     # Set Active to False (uncheck if checked)
    #     active_toggle = self.driver.find_element(*self.active_toggle)
    #     if active_toggle.is_selected() != vacancy['active']:
    #         active_toggle.click()
    #     # Set Publish to True
    #     publish_rss = self.driver.find_element(*self.publish_rss)
    #     if not publish_rss.is_selected() != vacancy['publish_in_RSS_Feb_and_Web_page']:
    #         publish_rss.click()
    #     # Save
    #     self.wait.until(EC.element_to_be_clickable(self.save_btn)).click()

    # def edit_vacancy(self):
    #     self.wait.until(EC.element_to_be_clickable(self.cancel_btn)).click()
    #     title = self.wait.until(EC.presence_of_element_located(self.edit_title))
    #     assert title.is_displayed(), "Không quay lại trang Vacancies sau khi Cancel"
    

        
    
    
    
        
        

    

    # def edit_vacancy(self):
    #     # self.wait.until(EC.visibility_of_element_located(self.edit_vacancy_page)).is_displayed()
    #     self.wait.until(EC.element_to_be_clickable(self.cancel_btn)).click()

    # def verify_vacancies_page(self):
    #     self.wait.until(EC.visibility_of_element_located(self.vacancies_page)).is_displayed()
    #     sleep(5)

    # def search_vacancy(self, job_title, hiring_manager):
    #     vacancy = ConfigReader.get_vacancy()
    #     self.wait.until(EC.element_to_be_clickable(self.job_title_dropdown)).click()
    #     self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//div[@role='listbox']//span[text()='{vacancy['job_title']}']"))).click()

    #     self.wait.until(EC.element_to_be_clickable(self.search_job_title)).click()
    #     self.driver.until(EC.visibility_of_element_located(By.XPATH, f"//data[@ Select()='{job_title}']")).click()
    #     self.wait.until(EC.element_to_be_clickable(self.search_hiring_manager)).send_keys(vacancy['hiring_manager'])
    #     self.driver.find_element(By.XPATH, f"//span[contains(text(), '{hiring_manager}')]").click()
    #     self.wait.until(EC.element_to_be_clickable(self.search_btn)).click()

    # def verify_vacancy_exists(self):
    #     assert self.wait.until(EC.presence_of_all_elements_located(self.vacancy_table)), "No vacancies found"

    # def verify_vacancy_data(self, vacancy_name, job_title, hiring_manager):
    #     assert self.wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='oxd-table-body']//div[contains(text(), '{vacancy_name}')]"))), f"Vacancy name {vacancy_name} not found"
    #     assert self.wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='oxd-table-body']//div[contains(text(), '{job_title}')]"))), f"Job title {job_title} not found"
    #     assert self.wait.until(EC.presence_of_element_located((By.XPATH, f"//div[@class='oxd-table-body']//div[contains(text(), '{hiring_manager}')]"))), f"Hiring manager {hiring_manager} not found"