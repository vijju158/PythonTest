import time
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.wikipedia.org/")
driver.maximize_window()
#Implicit wait
driver.implicitly_wait(10)
#Explicit wait------------
wait = WebDriverWait(driver, 10)

search = driver.find_element_by_xpath("//select[@id='searchLanguage']")
select = Select(search)
#select.select_by_visible_text("Eesti")
select.select_by_value("hi")

options = search.find_elements_by_tag_name("option")

for option in options:
    print("Text is : ", option.text, ", Lang is :"+option.get_attribute("lang"))

print("Total dropdown values are :", len(options))

block = driver.find_element_by_xpath("//*[@id=\"www-wikipedia-org\"]/div[7]/div[3]")
links = block.find_elements_by_tag_name("a")
print("1st link is : ", block.find_elements_by_tag_name("a").__getitem__(0).text)
print("10th link is : ", block.find_elements_by_tag_name("a").__getitem__(9).text)
block.find_elements_by_tag_name("a").__getitem__(9).click()

'''
print("-------------Printing all Links------------")

links = driver.find_elements_by_tag_name("a")

for link in links:
    print("Text is : ", link.text, ", URL is :"+link.get_attribute("href"))

print("Total Links in the page are :", len(links))
'''

#driver.quit()
