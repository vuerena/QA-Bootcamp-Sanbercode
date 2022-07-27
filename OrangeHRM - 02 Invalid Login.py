from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Test Case 02 - Invalid Login
#1) Buka browser Chrome
#2) Akses URL https://opensource-demo.orangehrmlive.com/
#3) Input username (Admin)
#4) Input password yang tidak sesuai (admin123456)
#5) Capture pesan error
#6) Verifikasi pesan error (Invalid credentials)
#8) Close browser

driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

elem = driver.find_element(By.NAME, 'txtUsername')
elem.clear()
elem.send_keys("Admin")
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.NAME, 'txtPassword')
elem.clear()
elem.send_keys("admin123456")
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.ID, 'spanMessage')
print(elem.text)

driver.close()