import pytest
import os
from pytest_bdd import scenarios, given, when,then, parsers
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

scenarios('../features/ahorcado.feature')

@pytest.fixture
def browser():
    # Initialize ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox");
    options.add_argument("--disable-dev-shm-usage");
    options.add_argument("--headless");

    driver = Chrome(options=options)

    # Wait implicitly for elements to be ready before attempting interactions
    driver.implicitly_wait(10)

    # Return the driver object at the end of setup
    yield driver

    # For cleanup, quit the driver
    driver.quit()

@given(parsers.parse('el comienzo de un nuevo juego con la palabra hola'))
def home(browser):
    url = os.getenv('URL_TEST')
    if url is None:
        url = 'http://localhost:5000'
    browser.get(url)
    browser.find_element_by_id('iniciar-link').click()

@when(parsers.parse("ingreso {letter}"))
def input_letter(browser, letter):
    input = browser.find_element_by_id('input-letra')
    input.send_keys(letter + Keys.RETURN)

@then('obtengo un mensaje de error')
def error_message(browser):
    result_message = browser.find_element_by_id('result-message')
    assert result_message.text == 'Error'

@then('obtengo un mensaje de acierto')
def ok_message(browser):
    result_message = browser.find_element_by_id('result-message')
    assert result_message.text == 'Muy bien!'

@then('gano la partida')
def won_game(browser):
    end_message = browser.find_element_by_id('won-text').text
    assert end_message == 'Ganaste'

@then(parsers.parse('me quedan {quantity_remaining} intentos restantes'))
def remaining_attempts(browser, quantity_remaining):
    end_message = browser.find_element_by_id('remaining-attempts').text
    assert end_message == quantity_remaining
