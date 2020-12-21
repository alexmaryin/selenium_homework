from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    credencials = ('div.form-group.first_class input[required]',
                   'div.form-group.second_class input[required]',
                   'div.form-group.third_class input[required]')
    browser = webdriver.Chrome()
    browser.get(link)

    for field in credencials:
        browser.find_element_by_tag_name(field).send_keys('fuck you')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(2)
    browser.quit()
