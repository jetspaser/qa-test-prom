"""
Модуль с описанием компонента футера (подвала) сайта.
"""
from playwright.sync_api import Page, Locator
from .base_page import BasePage

class Footer(BasePage):
    """
    Класс для взаимодействия с элементами в нижней части сайта.
    """

    def __init__(self, page: Page):
        """
        Инициализация локаторов футера.
        :param page: Объект страницы Playwright.
        """
        super().__init__(page)

        # 1. Ссылка на Telegram (используем класс social__link внутри li.telegram)
        self.tg_social_link: Locator = page.locator("li.telegram a.social__link")

        # 2. Текст "Сервис" (ищем ссылку с классом dark_link внутри блока title)
        self.service_link_text: Locator = page.locator(".title a.dark_link", has_text="Сервис")

    def click_telegram_social(self) -> None:
        """
        Выполняет клик по иконке Telegram в блоке соцсетей.
        """
        self.tg_social_link.scroll_into_view_if_needed()
        self.tg_social_link.click()