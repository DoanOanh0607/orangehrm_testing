from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.read_config import ConfigReader


class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, ConfigReader.get_timeout())
        self.admin_menu = (By.XPATH, "//span[text()='Admin']")
        

    def navigate_to_admin(self):
        self.wait.until(EC.element_to_be_clickable(self.admin_menu)).click()

    # def get_title_text(self):
    #     title = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h6")))
    #     return title.text

    # def add_user(self, user):
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Add']"))).click()

    #     # User Role
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='User Role']/following::div[contains(@class,'select-text-input')]"))).click()
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@role='option']//span[text()='{user['user_role']}']"))).click()

    #     # Employee Name
    #     emp_input = self.driver.find_element(By.XPATH, "//input[contains(@placeholder,'Type for hints')]")
    #     emp_input.send_keys(user["employee_name"])
    #     self.wait.until(EC.visibility_of_element_located((By.XPATH, f"//span[text()='{user['employee_name']}']"))).click()

    #     # Username
    #     self.driver.find_element(By.XPATH, "//label[text()='Username']/following::input[1]").send_keys(user["username"])

    #     # Status
    #     self.driver.find_element(By.XPATH, "//label[text()='Status']/following::div[contains(@class,'select-text-input')]").click()
    #     self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[@role='option']//span[text()='{user['status']}']"))).click()

    #     # Password + Confirm
    #     self.driver.find_element(By.XPATH, "//label[text()='Password']/following::input[1]").send_keys(user["password"])
    #     self.driver.find_element(By.XPATH, "//label[text()='Confirm Password']/following::input[1]").send_keys(user["password"])

    #     # Save
    #     self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']").click()

    # def search_user(self, username):
    #     self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='Username']/following::input[1]"))).send_keys(username)
    #     self.driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()

    #     results = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@role='rowgroup']/div[@role='row']")))
    #     assert any(username in r.text for r in results), f"Không tìm thấy user: {username}"
