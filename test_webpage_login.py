from selenium  import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_google():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    # driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
    driver.get("http://www.google.com")
    assert driver.title=="Google"
    driver.quit()

def test_google():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    # driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
    driver.get("http://www.google.com")
    assert driver.title=="Google"
    driver.quit()


def test_google():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    # driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
    driver.get("http://www.google.com")
    assert driver.title=="Google"
    driver.quit()

def test_Facbook():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    # driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
    driver.get("http://www.facebook.com")
    assert driver.title=="Facebook – log in or sign up"
    driver.quit()


def test_Innsta():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    # driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
    driver.get("http://www.Instagram.com")
    assert driver.title=="Instagram"
    driver.quit()

def test_gmail():
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    # driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
    driver.get("http://www.gmail.com")
    assert driver.title=="Gmail"
    driver.quit()
