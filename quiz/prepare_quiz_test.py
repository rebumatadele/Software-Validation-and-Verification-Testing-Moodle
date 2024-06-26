import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TestQuizPreparation(unittest.TestCase):
    def setUp(self):
        # Set up the webdriver (replace the path with the location of your chromedriver)
        self.driver = webdriver.Chrome()

    def test_quiz_preparation(self):
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

        # Navigate to the quiz page
        add_resource_button = self.driver.find_element(By.CSS_SELECTOR, 'a.add-activity-to-section')
        add_resource_button.click()
        quiz_option = self.driver.find_element(By.CSS_SELECTOR, 'a[data-type="quiz"]')
        quiz_option.click()

        # Fill in the quiz details
        quiz_name_field = self.driver.find_element(By.ID, 'id_name')
        quiz_name_field.send_keys('Test Quiz')
        quiz_description_field = self.driver.find_element(By.ID, 'id_introduction')
        quiz_description_field.send_keys('This is a test quiz.')
        save_button = self.driver.find_element(By.ID, 'id_submitbutton')
        save_button.click()

        # Wait for the quiz page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[title="Edit quiz"]')))

        # Add a question to the quiz
        add_question_button = self.driver.find_element(By.CSS_SELECTOR, 'a.addquestion')
        add_question_button.click()
        question_type_dropdown = self.driver.find_element(By.ID, 'id_qtype')
        question_type_dropdown.select_by_value('shortanswer')
        question_name_field = self.driver.find_element(By.ID, 'id_name')
        question_name_field.send_keys('What is the capital of France?')
        question_text_field = self.driver.find_element(By.ID, 'id_questiontext')
        question_text_field.send_keys('What is the capital of France?')
        question_answer_field = self.driver.find_element(By.ID, 'id_answer')
        question_answer_field.send_keys('Paris')
        save_question_button = self.driver.find_element(By.ID, 'id_submitbutton')
        save_question_button.click()

        # Verify the quiz and question
        quiz_title = self.driver.find_element(By.CSS_SELECTOR, 'h1.page-header-headings').text
        self.assertEqual(quiz_title, 'Test Quiz')
        question_text = self.driver.find_element(By.CSS_SELECTOR, 'div.qtext').text
        self.assertEqual(question_text, 'What is the capital of France?')

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()