from abc import ABC, abstractmethod

import allure
from playwright.sync_api import expect, Locator, Page

from logger import step


class BaseElement(ABC):
    def __init__(self, page: Page, selector: str, name: str, timeout: int = None):
        self.page: Page = page
        self.name: str = name
        self.selector: str = selector
        self.timeout: int = timeout

    @property
    @abstractmethod
    def type_of(self) -> str:
        return 'element'

    @property
    def locator(self) -> Locator:
        return self.page.locator(selector=self.selector).first

    def get_locator(self, **kwargs) -> Locator:
        selector = self.selector.format(**kwargs)
        return self.page.locator(selector=selector).first

    def get_text(self, **kwargs) -> str:
        locator = self.get_locator(**kwargs)
        return locator.inner_text(timeout=self.timeout)

    def click(self, count: int = 1) -> None:
        text = f'Clicking {self.type_of} {self.name}'
        with allure.step(text):
            step.info(text)
            self.get_locator().click(click_count=count, timeout=self.timeout)

    def double_click(self):
        text = f'Double-clicking {self.type_of} {self.name}'
        with allure.step(text):
            step.info(text)
            self.get_locator().dblclick()

    def hover(self) -> None:
        text = f'Hovering over {self.type_of} with name "{self.name}"'
        with allure.step(text):
            step.info(text)
            self.get_locator().hover()

    def should_be_visible(self, **kwargs) -> None:
        text = f'Checking that {self.type_of} "{self.name}" is visible'
        with allure.step(text):
            expect(self.get_locator()).to_be_visible(timeout=self.timeout)

    def should_have_text(self, value: str, **kwargs) -> None:
        text = f'Checking that {self.type_of} "{self.name}" has text "{value}"'
        with allure.step(text):
            step.info(text)
            expect(self.get_locator(**kwargs)).to_have_text(expected=value, timeout=self.timeout)

    def should_contain_text(self, value: str, **kwargs) -> None:
        text = f'Checking that {self.type_of} "{self.name}" contains text "{value}"'
        with allure.step(text):
            step.info(text)
            expect(self.get_locator(**kwargs)).to_contain_text(value, timeout=self.timeout)
