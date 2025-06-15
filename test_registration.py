from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import unittest
import os


class SeleniumDemoLoginTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://seleniumdemo.com/?page_id=7")
        self.driver.maximize_window()


    def test_registration(self):
        email = os.environ.get("EMAIL")
        password = os.environ.get("PASS")


        driver = self.driver

        # Find and fill username and password fields
        driver.find_element(By.ID, "reg_email").send_keys(email)
        driver.find_element(By.ID, "reg_password").send_keys(password)

        registration_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "register"))
        )

        # Click log in button
        registration_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()