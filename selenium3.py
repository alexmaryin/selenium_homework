import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/huge_form.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)
    inputs = browser.find_elements(By.TAG_NAME, 'input')
    for inp in inputs:
        inp.send_keys("fuck you!")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    print(browser.switch_to.alert.text)
finally:
    browser.quit()
