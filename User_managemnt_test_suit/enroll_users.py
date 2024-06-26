import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestEnrollUser(unittest.TestCase):
    def setUp(self):
        # Set up the webdriver (replace the path with the location of your chromedriver)
        self.driver = webdriver.Chrome()

    def test_enroll_user(self):
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

        # Navigate to the "Courses" page
        courses_link = self.driver.find_element(By.CSS_SELECTOR, 'a[data-key="coursemgmt"]')
        courses_link.click()

        # Find the "Test Course" and click on it
        course_list = self.driver.find_elements(By.CSS_SELECTOR, 'div.coursebox')
        for course in course_list:
            if 'Test Course' in course.text:
                course.click()
                break

        # Wait for the course page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.usertext')))

        # Navigate to the "Enrolled users" page
        enrolled_users_link = self.driver.find_element(By.CSS_SELECTOR, 'a[data-key="participants"]')
        enrolled_users_link.click()

        # Click the "Enroll users" button
        enroll_users_button = self.driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-primary')
        enroll_users_button.click()

        # Fill in the user details
        user_field = self.driver.find_element(By.ID, 'id_users')
        user_field.send_keys('rebuma_username')
        enroll_button = self.driver.find_element(By.ID, 'id_submitbutton')
        enroll_button.click()

        # Verify that the user was enrolled
        time.sleep(2)
        enrolled_users_list = self.driver.find_elements(By.CSS_SELECTOR, 'tr.user')
        self.assertTrue(any(user.text.startswith('rebuma') for user in enrolled_users_list))

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()