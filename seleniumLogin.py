from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch Chrome browser
driver = webdriver.Chrome()

# Open the URL
driver.get("http://127.0.0.1:5500/index.html")

# Find username and password inputs
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")

# Enter credentials
username_input.send_keys("waga")
password_input.send_keys("123")

# Submit the form
submit_button = driver.find_element(By.XPATH, "//button[@onclick='checkLogin()']")
submit_button.click()

# Wait for the message to appear
time.sleep(2)

# Get the response from the message div
message_div = driver.find_element(By.ID, "message")
response = message_div.text

# Print the response
print("Response:", response)

# Close the browser
driver.quit()
