import time
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://mail.google.com/mail/")
driver.maximize_window()
#Implicit wait
driver.implicitly_wait(10)

driver.find_element_by_xpath("//input[@id='identifierId']").send_keys("trainer@way2automation.com")
driver.find_element_by_xpath("//span[contains(text(),'Next')]").click()
#static wait---------
#time.sleep(10)

#Explicit wait------------
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"password\"]/div[1]/div/div[1]/input")))
element.send_keys("test")
#driver.find_element_by_xpath("//*[@id=\"password\"]/div[1]/div/div[1]/input").send_keys("test")

#driver.find_element_by_name("password").send_keys("test")

driver.find_element_by_xpath("//*[@id=\"passwordNext\"]/div/button/span").click()
time.sleep(5)
#errormsg=driver.find_element_by_xpath("//span[contains(text(),'Wrong password. Try again or click ‘Forgot password’ to reset it.')]").text
errormsg = driver.find_element_by_xpath("//*[@id=\"yDmH0d\"]/c-wiz/div/div[2]/div/div[1]/div/form/span/div[1]/div[2]/div[2]/span").text
print(errormsg)

driver.quit()
