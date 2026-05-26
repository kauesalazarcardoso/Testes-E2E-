from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_adicionar_produto_ao_carrinho(driver):

    login = LoginPage(driver)
    inventory = InventoryPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    inventory.add_first_product_to_cart()

    badge = inventory.get_cart_badge_number()

    assert badge == "1"