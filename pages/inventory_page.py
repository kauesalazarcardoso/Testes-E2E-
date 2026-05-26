from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button.btn_inventory")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    PRODUCT_TITLE = (By.CLASS_NAME, "inventory_item_name")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver

    def add_first_product_to_cart(self):
        self.driver.find_elements(*self.ADD_TO_CART_BUTTON)[0].click()

    def go_to_cart(self):
        self.driver.find_element(*self.CART_ICON).click()

    def get_product_name(self):
        return self.driver.find_elements(*self.PRODUCT_TITLE)[0].text

    def get_cart_badge_number(self):
        wait = WebDriverWait(self.driver, 5)
        return wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        ).text