import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

link = 'http://suninjuly.github.io/selects1.html'
link2 = 'http://suninjuly.github.io/selects2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link2)
    num1 = int(browser.find_element_by_id('num1').text)
    num2 = int(browser.find_element_by_id('num2').text)
    nums_sum = num1 + num2
    print('{} + {} = {}'.format(num1, num2, nums_sum))
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(str(nums_sum))
    browser.find_element_by_css_selector("button.btn").click()
    print(browser.switch_to.alert.text)
finally:
    time.sleep(2)
    browser.quit()
