import pytest
from selenium import webdriver
from orangehrm_automation.pages.login_page import LoginPage
from orangehrm_automation.pages.dashboard_page import DashboardPage
from orangehrm_automation.pages.pim_page import PimPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_orange_hrm_flow(driver):
    login_page = LoginPage(driver)
    dashboard = DashboardPage(driver)
    pim_page = PimPage(driver)

    # Step 1: Login
    login_page.load()
    login_page.login("Admin", "admin123")

    # Step 2: Go to PIM
    pim_page.go_to_pim()

    # Step 3: Add 3 Employees
    employees = [("Tony", "Stark"), ("Steve", "Rogers"), ("Bruce", "Banner")]
    for first, last in employees:
        pim_page.add_employee(first, last)

    # Step 4: Go to Employee List
    pim_page.go_to_employee_list()

    # Step 5: Verify Each Employee
    for first, last in employees:
        full_name = f"{first} {last}"
        assert pim_page.verify_employee(full_name), f"{full_name} was not found!"

    # Step 6: Logout
    dashboard.logout()
