import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCalendarEventCreation(unittest.TestCase):
    def setUp(self):
        # Set up the webdriver (replace the path with the location of your chromedriver)
        self.driver = webdriver.Chrome()

    def test_create_event(self):
        # Login as a user
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
        courses_link = self.driver.find_element(By.CSS_SELECTOR, 'a[data-key="schedule"]')
        courses_link.click()

        # Create a new event
        create_event_button = self.driver.find_element(By.ID, "create-event")
        create_event_button.click()

        # Fill in event details
        event_title_field = self.driver.find_element(By.ID, "event-title")
        event_title_field.send_keys("Test Event")

        start_date_field = self.driver.find_element(By.ID, "start-date")
        start_date_field.send_keys("2023-06-26")

        start_time_field = self.driver.find_element(By.ID, "start-time")
        start_time_field.send_keys("09:00")

        end_date_field = self.driver.find_element(By.ID, "end-date")
        end_date_field.send_keys("2023-06-26")

        end_time_field = self.driver.find_element(By.ID, "end-time")
        end_time_field.send_keys("11:00")

        save_button = self.driver.find_element(By.ID, "save-event")
        save_button.click()

        # Verify the event is displayed in the calendar
        wait = WebDriverWait(self.driver, 10)
        event_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"div.calendar-event[title='Test Event']")))
        self.assertIsNotNone(event_element)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()