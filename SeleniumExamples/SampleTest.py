
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="D:\Softwares\ChromeDriver\\chromedriver.exe")
driver.get("https://demo.guru99.com/v4/")
driver.maximize_window()

title = driver.title
print(title)
driver.find_element_by_name("uid").send_keys("mgr123")
driver.find_element_by_name("password").send_keys("mgr!23")
driver.find_element_by_name("btnLogin").click()
driver.find_element_by_xpath("//a[contains(@href,'addcustomerpage.php')]").click()
driver.find_element_by_name("name").send_keys("Test Customer")
driver.find_element_by_xpath("//input[@type='radio'][2]").click()
driver.find_element_by_name("dob").send_keys("01-01-1990")
driver.find_element_by_name("addr").send_keys("Test Address")
driver.find_element_by_name("city").send_keys("Test City")
driver.find_element_by_name("state").send_keys("Test State")
driver.find_element_by_name("pinno").send_keys("123456")
driver.find_element_by_name("telephoneno").send_keys("9999999999")
driver.find_element_by_name("emailid").send_keys("email@test.com")
driver.find_element_by_name("password").send_keys("mgr!23")
driver.find_element_by_name("sub").click()
#driver.close()
#driver.quit()
#body = driver.find_element_by_tag_name("body")
#body.send_keys(Keys.CONTROL + 'n')
#driver.execute_script("window.open('');")

#element = driver.find_element_by_xpath("//div[@id='dismiss-button']") #this element is visible
#driver.find_element_xpath("//div[@id='dismiss-button']").
add = driver.find_element_by_xpath("//*[@aria-label='Close ad']")
if add.is_displayed():
  add.click()
else:
  print("Element not found")