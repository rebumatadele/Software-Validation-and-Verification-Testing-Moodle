import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestAddCourse(unittest.TestCase):
    def setUp(self):
        # Set up the webdriver (replace the path with the location of your chromedriver)
        self.driver = webdriver.Chrome()

    def test_add_course(self):
        # Navigate to the Moodle demo site
        self.driver.get('https://school.moodledemo.net/login/index.php')

        # Wait for the page to load
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'username')))

        
        # Entering the login credentials
        username_field = self.driver.find_element(By.ID, 'username')
        password_field = self.driver.find_element(By.ID, 'password')
        username_field.send_keys('teacher')
        password_field.send_keys('moodle')
        login_button = self.driver.find_element(By.ID, 'loginbtn')
        login_button.click()

        # Wait for the dashboard page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.usertext')))

        # Navigate to the "Add a new course" page
        course_management_link = self.driver.find_element(By.CSS_SELECTOR, 'a[data-key="coursemgmt"]')
        course_management_link.click()
        add_course_button = self.driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-primary')
        add_course_button.click()

        # Fill in the course details
        course_full_name_field = self.driver.find_element(By.ID, 'id_fullname')
        course_short_name_field = self.driver.find_element(By.ID, 'id_shortname')
        course_summary_field = self.driver.find_element(By.ID, 'id_summary_editor')
        course_full_name_field.send_keys('Test Course')
        course_short_name_field.send_keys('TC')
        course_summary_field.send_keys('This is a test course.')
        create_course_button = self.driver.find_element(By.ID, 'id_submitbutton')
        create_course_button.click()

        # Verify that the course was created
        time.sleep(2)
        course_list = self.driver.find_elements(By.CSS_SELECTOR, 'div.coursebox')
        self.assertTrue(any(course.text.startswith('Test Course') for course in course_list))

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()