from selenium.webdriver.common.by import By


class CartPage:

    CART_ITEM = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "button.cart_button")

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        return self.driver.find_elements(*self.CART_ITEM)

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def remove_first_item(self):
        self.driver.find_elements(*self.REMOVE_BUTTON)[0].click()