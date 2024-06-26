from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TeacherCourseManagementTest(unittest.TestCase):
    def setUp(self):
        self.user_role = "teacher"
        self.username = "teacher"
        self.password = "moodle"

        # Initialize the WebDriver (replace with the path to your browser driver)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser
        self.driver.quit()

    def login_as(self, role, password):
        # Navigate to the login page
        self.driver.get('https://school.moodledemo.net/login/index.php')

        # Find the username and password fields and enter the credentials
        username_field = self.driver.find_element(By.ID, 'username')
        password_field = self.driver.find_element(By.ID, 'password')
        username_field.send_keys(role)
        password_field.send_keys(password)

        # Click the login button
        login_button = self.driver.find_element(By.ID, 'loginbtn')
        login_button.click()

        # Wait for the user's dashboard to load
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.mycourses')))

    def list_courses(self):
        # Navigate to the course list page
        self.driver.get('https://school.moodledemo.net/my/courses.php')

        # Find all the course cards
        course_cards = self.driver.find_elements(By.CSS_SELECTOR, 'div.card.coursebox')

        # Extract the course names from the cards
        course_names = [card.find_element(By.CSS_SELECTOR, 'h3.coursename').text for card in course_cards]

        # Print the course names
        for course_name in course_names:
            print(course_name)

    def access_course_details(self, course_name):
        # Navigate to the course list page
        self.driver.get('https://school.moodledemo.net/my/courses.php')

        # Find the course card with the given name
        course_card = next((card for card in self.driver.find_elements(By.CSS_SELECTOR, 'div.card.coursebox')
                            if card.find_element(By.CSS_SELECTOR, 'h3.coursename').text == course_name), None)

        if course_card:
            # Click on the course card to access the course details
            course_card.click()

            # Wait for the course page to load
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.course-content')))

            # Extract the course details
            course_details = {
                'name': self.driver.find_element(By.CSS_SELECTOR, 'h1.page-header-headings').text,
                'description': self.driver.find_element(By.CSS_SELECTOR, 'div.course-description').text,
                'activities': [activity.text for activity in self.driver.find_elements(By.CSS_SELECTOR, 'li.activity')]
            }

            return course_details
        else:
            print(f"Course '{course_name}' not found.")
            return None

    def test_course_management(self):
        try:
            # Login as a teacher
            self.login_as(self.username, self.password)

            # List the available courses
            self.list_courses()

            # Access the details of a specific course
            course_name = "Course 1"
            course_details = self.access_course_details(course_name)
            if course_details:
                print(f"Course Name: {course_details['name']}")
                print(f"Course Description: {course_details['description']}")
                print(f"Course Activities: {', '.join(course_details['activities'])}")

        except Exception as e:
            print(f"Error occurred during the test: {e}")
            raise

if __name__ == "__main__":
    unittest.main()