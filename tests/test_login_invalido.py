from pages.login_page import LoginPage


def test_login_invalido(driver):

    login_page = LoginPage(driver)
    login_page.open()

    login_page.login("standard_user", "senha_errada")

    error = login_page.get_error_message()

    assert "Username and password do not match" in error