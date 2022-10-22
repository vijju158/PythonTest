from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://gmail.com")
driver.find_element(By.ID,"identifierId").send_keys("trainer@way2automation.com")



