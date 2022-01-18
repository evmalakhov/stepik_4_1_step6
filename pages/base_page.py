from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class BasePage():

    def __init__(self, browser, url, login_link_selector, timeout=10):
        self.browser = browser
        self.url = url
        self.login_link_selector = login_link_selector
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def open(self):
        self.browser.get(self.url)

