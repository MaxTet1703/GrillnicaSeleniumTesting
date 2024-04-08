from src.config import driver, main_page
from src.pom import MainPage


def test_open_browser(driver):
    driver.get('https://krasnoyarsk.grilnica.ru/')
    
def test_open_shawerma_page(main_page):
    page = MainPage(main_page)
    assert page.is_shawerma_opened()

def test_open_rolls_page(main_page):
    page = MainPage(main_page)
    assert page.is_rolls_opened

def test_open_pizza_page(main_page):
    page = MainPage(main_page)
    assert page.is_pizza_opened

def test_open_wok_page(main_page):
    page = MainPage(main_page)
    assert page.is_wok_opened()

def test_open_free_page(main_page):
    page = MainPage(main_page)
    assert page.is_free_opened()

def test_open_hot_page(main_page):
    page = MainPage(main_page)
    assert page.is_hot_opened()

def test_open_drinks_page(main_page):
    page = MainPage(main_page)
    assert page.is_drinks_opened()

def test_open_combo_page(main_page):
    page = MainPage(main_page)
    assert page.is_combo_opened()

def test_good_search_food(main_page):
    page = MainPage(main_page)
    assert page.search_food("Охотничья")

def test_second_good_search_food(main_page):
    page = MainPage(main_page)
    assert page.search_food("Охот")

def test_bad_search_food(main_page):
    page = MainPage(main_page)
    assert not page.search_food("Озатничья")

def test_second_bad_search_food(main_page):
    page = MainPage(main_page)
    assert not page.search_food("Охотничя")

def test_open_modal_window(main_page):
    page = MainPage(main_page)
    assert page.open_modal_window_with_cities()

def test_good_city_modal_window_input(main_page):
    page = MainPage(main_page)
    assert page.search_city_into_modal_input("Красноярск")

def test_bad_city_modal_window_input(main_page):
    page = MainPage(main_page)
    assert not page.search_city_into_modal_input("Брнаул")






