from elements.button import Button
from elements.input import Input
from pages.base_page import BasePage
from playwright.sync_api import Page


class LoginPage(BasePage):

    def __init__(self, page: Page):
        super().__init__(page)
        self.username_input = Input(page, "//input[@id='sdo-login']", 'login')
        self.password_input = Input(page, "//input[@id='sdo-password']", 'password')
        self.login_button = Button(page, "//button/span[text()='Войти']", "Войти")
        self.recovery_button = Button(page, "//button/span[text()='Забыли пароль?']", "Забыли пароль?")

    def fill(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)

    def click_login_button(self):
        self.login_button.click()

    def click_recovery_button(self):
        self.recovery_button.click()
