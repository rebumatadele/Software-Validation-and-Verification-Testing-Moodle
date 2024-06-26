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

    def test_assignment_grading(self):
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

        # Check the submitted assignments
        submissions_link = self.driver.find_element(By.CSS_SELECTOR, 'a[title="View all submissions"]')
        submissions_link.click()

        # Locate the first submission
        first_submission = self.driver.find_element(By.CSS_SELECTOR, 'tr.submission:first-child')

        # Click the 'Grade' link for the first submission
        grade_link = first_submission.find_element(By.CSS_SELECTOR, 'a[title="Grade"]')
        grade_link.click()

        # Wait for the grading page to load
        wait.until(EC.presence_of_element_located((By.ID, 'id_grade')))

        # Enter a grade
        grade_field = self.driver.find_element(By.ID, 'id_grade')
        grade_field.clear()
        grade_field.send_keys('90')

        # Save the grade
        save_grade_button = self.driver.find_element(By.ID, 'id_submitbutton')
        save_grade_button.click()

        # Verify the updated grade
        updated_grade = self.driver.find_element(By.CSS_SELECTOR, 'div.submissionstatustable > div > div').text
        self.assertEqual(updated_grade, '90.0')

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()