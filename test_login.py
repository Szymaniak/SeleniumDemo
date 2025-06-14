from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import unittest

class SeleniumDemoLoginTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://seleniumdemo.com")
        self.driver.maximize_window()

    def test_login_button_present(self):

        print("Początek")

        driver = self.driver

        # Click on 'My Account' from the menu
        my_account = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/header/div[1]/div/div/div[1]/nav/div/ul/li[3]/a"))
        )
        my_account.click()

        # Find and fill username and password fields
        driver.find_element(By.ID, "username").send_keys("34t43rfwe4t3rfewf4w@test.com")
        driver.find_element(By.ID, "password").send_keys("34t43rfwe4t3rfewf4w")

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
        expected_text = "Hello 34t43rfwe4t3rfewf4w (not 34t43rfwe4t3rfewf4w? Log out)"

        # Assert the greeting text matches
        self.assertEqual(greeting.text.strip(), expected_text, "Greeting text does not match expected.")

        print("Koniec")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()