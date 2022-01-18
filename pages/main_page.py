from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
       login_link = self.browser.find_element(By.CSS_SELECTOR, self.login_link_selector)
       login_link.click() 

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, self.login_link_selector), f"Login link is not presented, CSS:\"{self.login_link_selector}\""

