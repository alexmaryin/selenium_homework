import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest
from selenium import webdriver

links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1']


def answer():
    return math.log(int(time.time()))


@pytest.fixture(scope="module")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('url', links)
def test_aliens_solve(browser, url):
    browser.get(url)
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'textarea')))
    browser.find_element(By.TAG_NAME, 'textarea').send_keys(str(answer()))
    browser.find_element(By.XPATH, "//button[text()= 'Отправить']").click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'div .smart-hints__hint')))
    text = browser.find_element(By.TAG_NAME, 'div .smart-hints__hint').text
    assert 'Correct!' in str(text), f'expected Correct! byt got: {text}'
