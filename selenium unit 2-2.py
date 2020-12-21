import os
import time
from selenium import webdriver

link = 'http://suninjuly.github.io/file_input.html'

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
open(file_path, 'a').close()

browser = webdriver.Chrome()
try:
    browser.get(link)
    browser.find_element_by_name('firstname').send_keys('Alex')
    browser.find_element_by_name('lastname').send_keys('Maryin')
    browser.find_element_by_name('email').send_keys('java73@yandex.ru')
    browser.find_element_by_id('file').send_keys(file_path)
    browser.find_element_by_css_selector("button.btn").click()
    print(browser.switch_to.alert.text)
finally:
    time.sleep(2)
    browser.quit()
