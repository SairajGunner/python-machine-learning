# https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test

# import all libraries
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
import time

# keep browser open even after script finishes executing
edge_options = Options()
# edge_options.add_argument('--headless')
edge_options.add_experimental_option("detach", True)

# launching the browser with additional options
driver = webdriver.Edge(options=edge_options)

# navigating to MyDC Home Page and navigating to Self-Service
driver.get("https://durhamcollege.ca/mydc/")
driver.find_element(By.PARTIAL_LINK_TEXT, 'SELF-SERVICE LOG IN').click()

# switching browser tab because previous click opens new tab
driver.switch_to.window(driver.window_handles[1])

# filling credentials and submitting login form
driver.find_element(By.ID, 'userNameInput').send_keys("username")
driver.find_element(By.ID, 'passwordInput').send_keys("password")

driver.find_element(By.ID, 'submitButton').send_keys(Keys.ENTER)

# navigating to the required document and clicking it
driver.find_element(By.PARTIAL_LINK_TEXT, 'Student Information').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'Canadian Tax Forms').click()
driver.find_element(By.PARTIAL_LINK_TEXT, 'T2202A Tax Credit Form').click()

driver.find_element(By.CSS_SELECTOR, ("input[type='submit']")).click()

# since the URL created is temporary - had to use GUI to download PDF - headless will not work
pyautogui.hotkey('ctrl', 's')
time.sleep(2)
path_and_filename = r'D:\Learning\AI ML\repos\python-starter\src\automation\test_data\tax_details.pdf'
pyautogui.typewrite(path_and_filename)
pyautogui.press('enter')
pyautogui.press('y')
