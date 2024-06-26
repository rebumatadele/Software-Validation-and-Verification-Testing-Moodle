import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestAddUser(unittest.TestCase):
    def setUp(self):
        # Set up the webdriver (replace the path with the location of your chromedriver)
        self.driver = webdriver.Chrome()

    def test_add_user(self):
        # Navigate to the Moodle demo site
        self.driver.get('https://school.moodledemo.net/login/index.php')

        # Wait for the page to load
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'username')))

        # Entering the login credentials (for an admin user)
        username_field = self.driver.find_element(By.ID, 'username')
        password_field = self.driver.find_element(By.ID, 'password')
        username_field.send_keys('manager')
        password_field.send_keys('moodle')
        login_button = self.driver.find_element(By.ID, 'loginbtn')
        login_button.click()

        # Wait for the dashboard page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.usertext')))

        # Navigate to the "Add a new user" page
        user_management_link = self.driver.find_element(By.CSS_SELECTOR, 'a[data-key="usermgmt"]')
        user_management_link.click()
        add_user_button = self.driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-primary')
        add_user_button.click()

        # Fill in the user details
        firstname_field = self.driver.find_element(By.ID, 'id_firstname')
        lastname_field = self.driver.find_element(By.ID, 'id_lastname')
        email_field = self.driver.find_element(By.ID, 'id_email')
        username_field = self.driver.find_element(By.ID, 'id_username')
        password_field = self.driver.find_element(By.ID, 'id_newpassword')
        firstname_field.send_keys('rebuma')
        lastname_field.send_keys('tadele')
        email_field.send_keys('rebuma.tadele@example.com')
        username_field.send_keys('rebuma_username')
        password_field.send_keys('moodle123')
        create_user_button = self.driver.find_element(By.ID, 'id_submitbutton')
        create_user_button.click()

        # Verify that the user was created
        time.sleep(2)
        user_list = self.driver.find_elements(By.CSS_SELECTOR, 'tr.user')
        self.assertTrue(any(user.text.startswith('rebuma') for user in user_list))

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()