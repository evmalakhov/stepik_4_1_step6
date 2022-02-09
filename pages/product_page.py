from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_not_be_success_product_name(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_PRODUCT_NAME), \
            "Success message is presented, but should not be"

    def should_disappear_success_product_name(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_PRODUCT_NAME), \
            "Success message is presented, but should disappear"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product Name not presented"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product Price not presented"

    def should_be_succes_product_name(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_PRODUCT_NAME), "Product Name notification not presented"

    def should_be_succes_product_price(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_PRODUCT_PRICE), "Product Price notification not presented"

    def is_success_name_correct(self):
        name_1 = self.get_product_name()
        name_2 = self.get_success_product_name()
        print(f"resulting product name correctness test \'{name_1}\' -- \'{name_2}\' ")
        assert name_1 == name_2 , f"Resulting Product Name mismatched"

    def is_success_price_correct(self):
        price_1 = self.get_product_price()
        price_2 = self.get_success_product_price()
        print(f"resulting product price correctness test \'{price_1}\' -- \'{price_2}\' ")
        assert price_1 == price_2 , f"Resulting Product Price mismatched"

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_success_product_price(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_PRODUCT_PRICE).text

    def get_success_product_name(self):
        return self.browser.find_element(*ProductPageLocators.SUCCESS_PRODUCT_NAME).text
