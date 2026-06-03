from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_fluxo_checkout_completo(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_first_product_to_cart()
    inventory.go_to_cart()

    cart.click_checkout()

    checkout.fill_form("Kaue", "Test", "95690000")
    checkout.continue_checkout()
    checkout.finish_checkout()

    message = checkout.get_success_message()

    assert "THANK YOU" in message.upper()