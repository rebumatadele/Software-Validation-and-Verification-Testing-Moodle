import unittest
from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRecurringCalendarEventCreation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_create_recurring_event(self):
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


        # Create a new recurring event
        create_event_button = self.driver.find_element(By.ID, "create-event")
        create_event_button.click()

        # Fill in event details
        event_title_field = self.driver.find_element(By.ID, "event-title")
        event_title_field.send_keys("Recurring Test Event")

        start_date = datetime.now() + timedelta(days=7)
        end_date = start_date + timedelta(hours=2)

        start_date_field = self.driver.find_element(By.ID, "start-date")
        start_date_field.send_keys(start_date.strftime("%Y-%m-%d"))

        start_time_field = self.driver.find_element(By.ID, "start-time")
        start_time_field.send_keys(start_date.strftime("%H:%M"))

        end_date_field = self.driver.find_element(By.ID, "end-date")
        end_date_field.send_keys(end_date.strftime("%Y-%m-%d"))

        end_time_field = self.driver.find

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()