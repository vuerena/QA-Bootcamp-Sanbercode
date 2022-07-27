from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Test Case 04 - Valid Login
#1) Buka browser Chrome
#2) Akses URL https://www.saucedemo.com/
#3) Input username (problem_user)
#4) Input password (secret_sauce)
#5) Login
#6) Capture judul homepage
#7) Verifikasi judul homepage (Swag Labs)
#8) Close browser

driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")

driver.get("https://www.saucedemo.com/")

elem = driver.find_element(By.NAME, 'user-name')
elem.clear()
elem.send_keys("problem_user")
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.NAME, 'password')
elem.clear()
elem.send_keys("secret_sauce")
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.ID, 'login-button')
elem.click()

actual_title = driver.title
expected_title = "Swag Labs"

if actual_title==expected_title:
    print("Valid Login Passed")
else:
    print("Valid Login Failed")

driver.close()