from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_validar_item_no_carrinho(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_first_product_to_cart()
    inventory.go_to_cart()

    items = cart.get_cart_items()

    assert len(items) == 1