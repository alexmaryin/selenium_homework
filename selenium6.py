import math
import time
from selenium import webdriver


link = 'http://suninjuly.github.io/math.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    answer = calc(browser.find_element_by_id('input_value').text)
    browser.find_element_by_id('answer').send_keys(answer)
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector("button.btn").click()
    print(browser.switch_to.alert.text)
finally:
    time.sleep(2)
    browser.quit()
