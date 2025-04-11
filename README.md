# OrangeHRM Web Automation with Selenium (POM-Based)

This project automates the core workflows of the OrangeHRM web application using **Selenium**, **PyTest**, and the **Page Object Model (POM)** design pattern.

## ✨ Features Automated
- Login to OrangeHRM
- Navigate to the PIM module
- Add multiple employees
- Navigate to the Employee List
- Verify if employees were successfully added
- Logout
- ## 🛠️ Tech Stack
- Python 3.11
- Selenium WebDriver
- PyTest
- Page Object Model (POM)

## 🗂️ Project Structure
ohrm3/
├── tests/
│   └── test_orangehrm.py
├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   ├── pim_page.py
│   └── base_page.py
└── conftest.py

**##Set Up Virtual Environment (Optional but Recommended)**
python -m venv venv
venv\Scripts\activate  # For Windows
**##Install Dependencies**
pip install -r requirements.txt
**Sample requirements.txt:**
selenium
pytest
**##Run the Test**
pytest -v
**Notes**
Make sure Chrome is installed and the ChromeDriver is compatible with your browser version.

You can change employee names or credentials inside the test file: test_orangehrm.py.

If employee verification fails, ensure that the PIM list is properly loaded and selectors are correct.
