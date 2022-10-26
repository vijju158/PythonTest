import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


def get_data():

    return [
        ("trainer@test.com","sdfffsf"),
        ("helper@test.com", "sdxvvfffsf"),
        ("user@test.com", "gdgdfgsf")
    ]

def setup_function():
    global driver
    driver = webdriver.Chrome(executable_path="D:\\Softwares\\ChromeDriver\\chromedriver.exe")
    driver.get("http://facebook.com")
    driver.maximize_window()

def teardown_function():
    driver.quit()



@pytest.mark.parametrize("username,password", get_data())
def test_doLogin(username, password):
    driver.find_element(By.ID,"email").send_keys(username)
    driver.find_element(By.ID,"email").send_keys(password)
