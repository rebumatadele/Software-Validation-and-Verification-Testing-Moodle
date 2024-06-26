import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestAssignmentGrading(unittest.TestCase):
    def setUp(self):
        # Set up the webdriver (replace the path with the location of your chromedriver)
        self.driver = webdriver.Chrome()

    def test_add_inline_comment(self):
        # Navigate to the Moodle demo site
        self.driver.get('https://school.moodledemo.net/login/index.php')

        # Wait for the page to load
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'username')))

        # Entering the login credentials (for a teacher user)
        username_field = self.driver.find_element(By.ID, 'username')
        password_field = self.driver.find_element(By.ID, 'password')
        username_field.send_keys('teacher')
        password_field.send_keys('moodle')
        login_button = self.driver.find_element(By.ID, 'loginbtn')
        login_button.click()

        # Wait for the dashboard page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.usertext')))

        # Navigate to the "Test Course"
        courses_link = self.driver.find_element(By.CSS_SELECTOR, 'a[data-key="coursemgmt"]')
        courses_link.click()
        course_link = self.driver.find_element(By.CSS_SELECTOR, 'a[title="Test Course"]')
        course_link.click()

        # Navigate to the assignment page
        assignment_link = self.driver.find_element(By.CSS_SELECTOR, 'a[title="Assignment example"]')
        assignment_link.click()

        # Click the 'View x submitted assignments' link and then the 'Grade' link for a submission
        submitted_assignments_link = self.driver.find_element(By.CSS_SELECTOR, 'a.submissionstatuslink')
        submitted_assignments_link.click()
        grade_link = self.driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-primary')
        grade_link.click()

        # Add an inline comment and save the changes
        inline_comment_field = self.driver.find_element(By.ID, 'id_addcomment')
        inline_comment_field.send_keys('This is a test inline comment.')
        save_changes_button = self.driver.find_element(By.ID, 'id_submitbutton')
        save_changes_button.click()

        # Verify the updated 'Last modified (Teacher)' date and the link text change from 'Grade' to 'Update'
        last_modified_date = self.driver.find_element(By.CSS_SELECTOR, 'td.cell.c4').text
        self.assertTrue('Last modified' in last_modified_date)
        grade_status_link = self.driver.find_element(By.CSS_SELECTOR, 'a.btn.btn-primary')
        self.assertEqual(grade_status_link.text, 'Update')

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()