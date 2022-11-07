from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


# def is_element_present(id):
#     try:
#         driver.find_element_by_id(id)
#         return True
#     except NoSuchElementException:
#         return False

# def is_element_present(how, what):
#     try:
#         driver.find_element(by=how, value=what)
#         return True
#     except NoSuchElementException:
#         return False

def is_element_present(how, what):
    if len(driver.find_elements(by=how, value=what)) ==0:
        return False
    else:
        return True


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://mail.google.com/mail/")
driver.maximize_window()
#Implicit wait
driver.implicitly_wait(1)
#Explicit wait------------
wait = WebDriverWait(driver, 1)

print(driver.find_element_by_id("identifierId").is_displayed())
print(driver.find_element_by_id("identifierId").is_enabled())

#print(is_element_present("identifierI"))
print(is_element_present(By.ID,"identifierId"))
print(is_element_present(By.XPATH,"//input[@id='identifierId21']"))

