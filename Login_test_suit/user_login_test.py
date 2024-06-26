from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.user_role = self.display_menu()

        # Initialize the WebDriver (replace with the path to your browser driver)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        # Close the browser
        self.driver.quit()

    def test_login(self):
        self.login_as(self.user_role, "moodle")

    def login_as(self, user, password):
        try:
            # Navigate to the login page
            self.driver.get('https://school.moodledemo.net/login/index.php')

            # Wait for the page to load
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.ID, 'username')))

            # Enter the username and password
            username_field = self.driver.find_element(By.ID, 'username')
            password_field = self.driver.find_element(By.ID, 'password')

            username_field.send_keys(user)
            password_field.send_keys(password)

            # Click the login button
            login_button = self.driver.find_element(By.ID, 'loginbtn')
            login_button.click()

            # Wait for my courses page to load
            wait.until(EC.presence_of_element_located((By.ID, 'page-wrapper')))

            # Verify that the user is logged in
            if 'My courses | Mount Orange School' in self.driver.title:
                print("Test case passed")
            else:
                print("Test case failed")
            self.assertTrue('My courses | Mount Orange School' in self.driver.title)
        except Exception as e:
            print(f"Error occurred during login as {user}: {e}")
            raise

    def display_menu(self):
        print("Select the user role to test:")
        print("1. Student")
        print("2. Teacher")
        print("3. Manager")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            return "student"
        elif choice == "2":
            return "teacher"
        elif choice == "3":
            return "manager"
        else:
            print("Invalid choice. Exiting...")
            exit()
        return choice


if __name__ == "__main__":
    unittest.main()
