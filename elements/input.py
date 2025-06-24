import allure
from playwright.sync_api import expect

from elements.base_element import BaseElement
from logger import step


class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return 'input'

    def fill(self, value: str | int | float, validate_value=False):
        value = str(value)
        text = f'Fill {self.type_of} "{self.name}" to value "{value}"'
        with allure.step(text):
            self.get_locator().fill(value=value, timeout=self.timeout)
            step.info(text)
            if validate_value:
                self.should_have_value(value=value)

    def should_have_value(self, value: str):
        text = f'Checking that {self.type_of} "{self.name}" has a value "{value}"'
        with allure.step(text):
            step.info(text)
            expect(self.get_locator()).to_have_value(value=value, timeout=self.timeout)

    def get_value(self) -> str:
        action_text = f'Get value from {self.type_of} "{self.name}"'
        with allure.step(action_text):
            step.info(action_text)
            return self.get_locator().input_value(timeout=self.timeout)
