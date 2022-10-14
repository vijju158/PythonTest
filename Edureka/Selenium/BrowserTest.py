
from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\Softwares\ChromeDriver\\chromedriver.exe")
driver.get("https://demo.guru99.com/v4/")
driver.maximize_window()
title=driver.title
print(driver.title)
assert "Guru99" in title
driver.close()