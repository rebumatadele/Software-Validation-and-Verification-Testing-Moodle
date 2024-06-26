import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestAssignmentSubmission(unittest.TestCase):
    def setUp(self):
        # Set up the webdriver (replace the path with the location of your chromedriver)
        self.driver = webdriver.Chrome()

    def test_assignment_submission(self):
        # Navigate to the Moodle demo site
        self.driver.get('https://school.moodledemo.net/login/index.php')

        # Wait for the page to load
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, 'username')))

        # Entering the login credentials (for a student user)
        username_field = self.driver.find_element(By.ID, 'username')
        password_field = self.driver.find_element(By.ID, 'password')
        username_field.send_keys('student')
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

        # Click the 'Add submission' button
        add_submission_button = self.driver.find_element(By.CSS_SELECTOR, 'button#add-file-btn')
        add_submission_button.click()

        # Upload a file as the assignment submission
        file_input = self.driver.find_element(By.CSS_SELECTOR, 'input#id_files_filemanager')
        file_input.send_keys('/path/to/your/file.pdf')
        save_changes_button = self.driver.find_element(By.ID, 'id_submitbutton')
        save_changes_button.click()

        # Verify the successful submission
        submission_status = self.driver.find_element(By.CSS_SELECTOR, 'div.submissionstatustable > div > div').text
        self.assertEqual(submission_status, 'Submitted for grading')

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()