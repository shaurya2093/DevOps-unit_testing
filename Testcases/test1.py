#testcases using selenium


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver (here using Chrome)
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in your PATH

# Open your website (replace with your actual URL)
driver.get("http://localhost:8081")

# Maximize the browser window (optional)
driver.maximize_window()

# Wait for the page to load
time.sleep(2)  # Use WebDriverWait for better handling in real cases

# Example 1: Check if the page title is correct
expected_title = "Your Website Title"  # Replace with the actual title
assert expected_title in driver.title, f"Expected title: {expected_title}, but got: {driver.title}"

# Example 2: Find an element by ID and interact with it
search_box = driver.find_element(By.ID, "search-box")  # Replace with actual element ID
search_box.send_keys("Some search term")  # Simulate typing in the search box
search_box.send_keys(Keys.RETURN)  # Press Enter to submit

# Example 3: Wait for results and verify an element
time.sleep(3)  # Use WebDriverWait instead of sleep in production code
result_text = driver.find_element(By.ID, "result-id").text  # Replace with actual result element ID
assert "Expected Result" in result_text, f"Expected 'Expected Result' but got: {result_text}"

# Example 4: Fill out a form (e.g., contact form)
name_field = driver.find_element(By.NAME, "name")  # Replace with actual field name
email_field = driver.find_element(By.NAME, "email")  # Replace with actual field name
submit_button = driver.find_element(By.ID, "submit-btn")  # Replace with actual submit button ID

name_field.send_keys("Test User")
email_field.send_keys("testuser@example.com")
submit_button.click()

# Wait for form submission
time.sleep(2)

# Example 5: Verify successful form submission
success_message = driver.find_element(By.ID, "success-message").text  # Replace with actual success message ID
assert "Thank you for contacting us" in success_message, f"Expected success message, but got: {success_message}"

# Close the browser after the test
driver.quit()
