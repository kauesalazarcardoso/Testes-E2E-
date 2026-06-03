from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def fill_form(self, first, last, postal):
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME)).send_keys(first)
        self.wait.until(EC.visibility_of_element_located(self.LAST_NAME)).send_keys(last)
        self.wait.until(EC.visibility_of_element_located(self.POSTAL_CODE)).send_keys(postal)

    def continue_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON)).click()

    def finish_checkout(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        ).text