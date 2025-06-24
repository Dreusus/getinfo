from elements.input import Input
from pages.base_page import BasePage
from playwright.sync_api import Page

class LoginPage(BasePage):

    def __init__(self,page:Page):
        super().__init__(page)
        self.login_input = Input(page,"//input[@id='sdo-login']",'login')
        self.password_input = Input(page,"//input[@id='sdo-password']",'password')
