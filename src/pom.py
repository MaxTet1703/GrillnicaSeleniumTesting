import time

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains



class MainPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def is_shawerma_opened(self):
        button = self.driver.find_element(by=By.ID, value="shawarma")
        self.driver.execute_script("arguments[0].click();", button)    
        return self.driver.current_url.endswith("shawarma")
    
    def is_pizza_opened(self):
        button = self.driver.find_element(by=By.ID, value="pizza")
        self.driver.execute_script("arguments[0].click();", button)
        return self.driver.current_url.endswith("pizza")
    
    def is_rolls_opened(self):
        button = self.driver.find_element(by=By.ID, value="rolls")
        self.driver.execute_script("arguments[0].click();", button)
        return self.driver.current_url.endswith("rolls")

    def is_wok_opened(self):
        button = self.driver.find_element(by=By.ID, value="wok")
        self.driver.execute_script("arguments[0].click();", button)
        return self.driver.current_url.endswith("wok")
    
    def is_free_opened(self):
        button = self.driver.find_element(by=By.ID, value="free")
        self.driver.execute_script("arguments[0].click();", button)
        return self.driver.current_url.endswith("free")
    
    def is_hot_opened(self):
        button = self.driver.find_element(by=By.ID, value="hot")
        self.driver.execute_script("arguments[0].click();", button)
        return self.driver.current_url.endswith("hot")

    def is_drinks_opened(self):
        button = self.driver.find_element(by=By.ID, value="drinks")
        self.driver.execute_script("arguments[0].click();", button)
        return self.driver.current_url.endswith("drinks")

    def is_combo_opened(self):
        button = self.driver.find_element(by=By.ID, value="combo")
        self.driver.execute_script("arguments[0].click();", button)
        return self.driver.current_url.endswith("combo")
        
    def search_food(self, text):
        form_input = self.driver.find_element(by=By.NAME, value="search")
        form_input.send_keys(text)
        form_input.send_keys(Keys.ENTER)
        list_of_food = self.driver.find_elements(by=By.CSS_SELECTOR, value="div.product-list")
        return list_of_food

    def search_city_into_modal_input(self, text):
        button = self.driver.find_elements(by=By.CSS_SELECTOR, value="span.button-content")[0]
        ActionChains(self.driver).click(button).perform()
        # self.driver.find_elements(by=By.CSS_SELECTOR, value="div.gr-modal.open")[0]
        input_search = self.driver.find_element(by=By.NAME, value="search-city")
        input_search.send_keys(text)
    
        return self.driver.find_elements(by=By.CSS_SELECTOR, value=".select-city-modal-item")

    def open_modal_window_with_cities(self):
        button = self.driver.find_elements(by=By.CSS_SELECTOR, value="span.button-content")[0]
        self.driver.execute_script("arguments[0].click();", button)
        modal = self.driver.find_elements(by=By.CSS_SELECTOR, value="div.gr-modal")[0]
        return 'open' in modal.get_attribute('class').split(' ')
