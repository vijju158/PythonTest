from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#selenium 3
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

#selenium 4
#s = Service(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=s)
#s=Service(executable_path=ChromeDriverManager().install())
#driver = webdriver.Chrome(service=s)
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



#Executable path
#driver = webdriver.Chrome(executable_path="D:\Softwares\ChromeDriver\\chromedriver.exe")
driver.get("https://way2automation.com")
driver.maximize_window()
title = driver.title
print(title)
assert "Selenium" in title
driver.close()