import unittest

from selenium import webdriver

links = ("http://suninjuly.github.io/registration1.html",
         "http://suninjuly.github.io/registration2.html")

credencials = ('div.form-group.first_class input[required]',
               'div.form-group.second_class input[required]',
               'div.form-group.third_class input[required]')


class TestAbs(unittest.TestCase):
    def test_find_lastname1(self):
        browser = webdriver.Chrome()
        browser.get(links[0])
        for field in credencials:
            browser.find_element_by_tag_name(field).send_keys('test data')
        browser.find_element_by_css_selector("button.btn").click()
        welcome_text = browser.find_element_by_tag_name("h1").text
        self.assertIn("successfully", welcome_text, "Error with login")
        browser.quit()

    def test_find_lastname2(self):
        browser = webdriver.Chrome()
        browser.get(links[1])
        for field in credencials:
            browser.find_element_by_tag_name(field).send_keys('test data')
        browser.find_element_by_css_selector("button.btn").click()
        welcome_text = browser.find_element_by_tag_name("h1").text
        self.assertIn("successfully", welcome_text, "Error with login")
        browser.quit()


if __name__ == "__main__":
    unittest.main()
