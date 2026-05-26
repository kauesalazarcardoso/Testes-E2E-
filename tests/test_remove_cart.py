from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_remover_item_carrinho(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)
    cart = CartPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_first_product_to_cart()
    inventory.go_to_cart()

    cart.remove_first_item()

    assert len(cart.get_cart_items()) == 0