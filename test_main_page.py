import time 
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"; login_link_selector = "#login_link"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"; login_link_selector = "#registration_link"
    page = MainPage(browser, link, login_link_selector)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()

    time.sleep(10)

