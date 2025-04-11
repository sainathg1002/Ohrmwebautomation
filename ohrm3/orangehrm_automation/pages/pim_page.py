from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators
        self.pim_tab = (By.XPATH, "//span[text()='PIM']")
        self.add_employee_button = (By.LINK_TEXT, "Add Employee")
        self.first_name_input = (By.NAME, "firstName")
        self.last_name_input = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.employee_list_tab = (By.LINK_TEXT, "Employee List")
        self.search_box = (By.XPATH, "//input[@placeholder='Search']")
        self.employee_rows = (By.XPATH, "//div[@class='oxd-table-card']")

    def go_to_pim(self):
        self.wait.until(EC.element_to_be_clickable(self.pim_tab)).click()

    def add_employee(self, first_name, last_name):
        self.wait.until(EC.element_to_be_clickable(self.add_employee_button)).click()

        self.wait.until(EC.visibility_of_element_located(self.first_name_input)).send_keys(first_name)
        self.wait.until(EC.visibility_of_element_located(self.last_name_input)).send_keys(last_name)

        self.wait.until(EC.element_to_be_clickable(self.save_button)).click()

    def go_to_employee_list(self):
        self.wait.until(EC.element_to_be_clickable(self.employee_list_tab)).click()

    def verify_employee(self, name):
        self.wait.until(EC.presence_of_all_elements_located(self.employee_rows))
        employees = self.driver.find_elements(*self.employee_rows)
        for emp in employees:
            if name in emp.text:
                print(f"{name} Verified")
                return True
        print(f"{name} Not Found")
        return False
