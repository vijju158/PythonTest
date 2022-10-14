
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#driver = webdriver.Chrome(executable_path="D:\Softwares\ChromeDriver\\chromedriver.exe")
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get("https://demo.guru99.com/v4/")
driver.maximize_window()
title=driver.title
print(driver.title)
assert "Guru99" in title
driver.close()