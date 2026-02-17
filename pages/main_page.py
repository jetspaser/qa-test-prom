"""
MainPage.

Page Object главной страницы сайта.
Содержит методы для взаимодействия
с основными элементами главной страницы.
"""

from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.header import Header


class MainPage(BasePage):
    """
    Главная страница сайта https://promminer.ru
    """

    URL = "https://promminer.ru/"

    def __init__(self, page: Page) -> None:
        super().__init__(page)
        self.header = Header(page)

    def open(self, url) -> None:
        """
        Открыть главную страницу сайта.
        """
        self.page.goto(self.URL)
