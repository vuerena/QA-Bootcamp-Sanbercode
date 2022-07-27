from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Test Case 05 - Invalid Login
#1) Buka browser Chrome
#2) Akses URL https://www.saucedemo.com/
#3) Input username (problem_user)
#4) Input password yang tidak sesuai (123456)
#5) Capture pesan error
#6) Verifikasi pesan error (Invalid credentials)
#8) Close browser

driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")

driver.get("https://www.saucedemo.com/")

elem = driver.find_element(By.NAME, 'user-name')
elem.clear()
elem.send_keys("problem_user")
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.NAME, 'password')
elem.clear()
elem.send_keys("123456")
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.ID, 'login-button')
elem.click()

error_elem = driver.find_element(By.CLASS_NAME, 'error-button')
error_elem = error_elem.is_displayed()
if error_elem == True:
    print("Passed")
else:
    print("Failed")

driver.close()