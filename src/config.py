import time
from pathlib import Path

from pytest import fixture
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

@fixture(scope="session")
def driver():
    service = Service(executable_path=Path().cwd() / "chromedriver" / "chromedriver")
    driver = Chrome(service=service)
    driver.maximize_window()
    driver.implicitly_wait(2) 
    return driver

@fixture(scope="function")
def main_page(driver):
    driver.get("https://krasnoyarsk.grilnica.ru")
    return driver

