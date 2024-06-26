from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

# opening Chrome browser

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://school.moodledemo.net/login/index.php")

# finding the username and password fields and entering the values
username_field = driver.find_element(By.ID, "username")
username_field.send_keys("student")
sleep(5)

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("moodle")
sleep(5)

# clicking the "Log in" button
login_button = driver.find_element(By.ID, "loginbtn")
login_button.click()
sleep(5)

# wait for the page to load
sleep(100)