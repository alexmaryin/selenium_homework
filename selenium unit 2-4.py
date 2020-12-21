import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


link = 'http://suninjuly.github.io/execute_script.html'
alert_link = 'http://suninjuly.github.io/alert_accept.html'
windowed_link = 'http://suninjuly.github.io/redirect_accept.html'
book_link = 'http://suninjuly.github.io/explicit_wait2.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


def calc_and_print(driver):
    answer = calc(driver.find_element_by_id('input_value').text)
    driver.find_element_by_id('answer').send_keys(answer)
    driver.find_element_by_id('solve').click()
    return driver.switch_to.alert.text


def scroll_to(driver, element):
    driver.execute_script('return arguments[0].scrollIntoView(true);', element)
    return element


def main():
    browser = webdriver.Chrome()
    try:
        browser.get(book_link)
        WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
        browser.find_element(By.ID, 'book').click()
        print(calc_and_print(browser))
    finally:
        time.sleep(2)
        browser.quit()


if __name__ == '__main__':
    main()
