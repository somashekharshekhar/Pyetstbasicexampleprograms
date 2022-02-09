from selenium  import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import time
driver=None


def setup_module(module):
    global driver
    driver=webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("http://www.google.com")


def teardown_module(module):
    driver.quit()


def test_google_title():
    assert driver.title=="Google"


def test_google_url():
    assert driver.current_url=='https://www.google.com/?gws_rd=ssl'
