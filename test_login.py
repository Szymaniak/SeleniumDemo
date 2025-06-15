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
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://seleniumdemo.com/?page_id=7")
        self.driver.maximize_window()

    def test_01_registration(self):
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

    def test_02_login_button_present(self):
        email = os.environ.get("EMAIL")
        password = os.environ.get("PASS")

        print("Początek")

        driver = self.driver


        # Find and fill username and password fields
        driver.find_element(By.ID, "username").send_keys(email)
        driver.find_element(By.ID, "password").send_keys(password)

        # Wait for the login button to appear
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/article/div/section/div/div/div[2]/div[1]/form/p[3]/button"))
        )

        # Click log in button
        login_button.click()

        # Wait for greeting element after login
        greeting = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div[2]/div/div/article/div/section/div/div/div/p[1]"))
        )

        # Expected greeting message
        trimmed_email = email.split("@")[0]
        expected_text = "Hello "+trimmed_email+" (not "+trimmed_email+"? Log out)"

        # Assert the greeting text matches
        self.assertEqual(greeting.text.strip(), expected_text, "Greeting text does not match expected.")

        print("Koniec")


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()