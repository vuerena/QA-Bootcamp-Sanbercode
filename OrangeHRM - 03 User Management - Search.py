from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#Test Case 03 - User Management - Search
#1) Buka browser Chrome
#2) Akses URL https://opensource-demo.orangehrmlive.com/
#3) Input username (Admin)
#4) Input password (admin123)
#5) Login
#6) Masuk halaman User Management dengan mengakses ke URL https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers
#7) Input username yang akan dicari (Aravind)
#8) Klik Search
#9) Verifikasi apakah tabel hasil pencarian ditampilkan
#10) Close browser

driver = webdriver.Chrome("C:\Drivers\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/")

elem = driver.find_element(By.NAME, 'txtUsername')
elem.clear()
elem.send_keys("Admin")
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.NAME, 'txtPassword')
elem.clear()
elem.send_keys("admin123")
elem.send_keys(Keys.RETURN)

driver.get("https://opensource-demo.orangehrmlive.com/index.php/admin/viewSystemUsers")

elem = driver.find_element(By.ID, 'searchSystemUser_userName')
elem.clear()
elem.send_keys("Aravind")
elem.send_keys(Keys.RETURN)

elem = driver.find_element(By.ID, 'searchBtn')
elem.click()
#elem.send_keys(Keys.RETURN)

search_elem = driver.find_element(By.ID, 'search-results')
search_elem = search_elem.is_displayed()
if search_elem == True:
    print("Passed")
else:
    print("Failed")

driver.close()