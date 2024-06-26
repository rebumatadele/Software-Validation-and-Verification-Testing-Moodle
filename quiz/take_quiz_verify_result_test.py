import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestQuizTaking(unittest.TestCase):
    def setUp(self):
        # Set up the webdriver (replace the path with the location of your chromedriver)
        self.driver = webdriver.Chrome()

    def test_quiz_taking(self):
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

        # Navigate to the quiz page
        quiz_link = self.driver.find_element(By.CSS_SELECTOR, 'a[title="Test Quiz"]')
        quiz_link.click()

        # Wait for the quiz page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'form#responseform')))

        # Answer the question
        question_input = self.driver.find_element(By.ID, 'id_answer')
        question_input.send_keys('Paris')
        submit_button = self.driver.find_element(By.ID, 'id_submitbutton')
        submit_button.click()

        # Wait for the results page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.grade')))

        # Verify the result
        result = self.driver.find_element(By.CSS_SELECTOR, 'div.grade').text
        self.assertEqual(result, 'Grade: 1 out of 1')

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()