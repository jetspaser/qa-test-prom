

"""
Модуль с описанием компонента Header (шапка сайта).
Содержит элементы, доступные на всех страницах сайта.
"""
from playwright.sync_api import Page, Locator
from .base_page import BasePage


class Header(BasePage):
    """
    Класс для взаимодействия с шапкой сайта: поиск, каталог, контакты.
    """

    def __init__(self, page: Page):
        """
        Инициализация локаторов хедера.
        :param page: Объект страницы Playwright.
        """
        super().__init__(page)

        # 1. Поле ввода поиска (ID стабилен)
        self.search_input: Locator = page.locator("#title-search-input")

        # 2. Кнопка "Лупа" 
        # ИСПРАВЛЕНИЕ: Уточняем путь. Берем кнопку поиска именно внутри блока #title-search,
        # чтобы избежать конфликта с мобильной и фиксированной версиями.
        self.search_button: Locator = page.locator("#title-search button[name='s']")

        # 3. Кнопка "Каталог" 
        self.catalog_button: Locator = page.locator("header").get_by_text("Каталог", exact=True).first

        # 4. Ссылка на Telegram
        self.telegram_icon: Locator = page.locator("header a[href*='t.me']")

        # 5. Кнопка "Заказать звонок"
        self.callback_button: Locator = page.locator("header").get_by_text("Заказать звонок")

    def search(self, text: str, use_mouse: bool = False) -> None:
        """
        Выполняет поиск товара.
        :param text: Текст поискового запроса.
        :param use_mouse: Если True — кликаем по лупе. Если False — жмем Enter.
        """
        self.search_input.fill(text)

        if use_mouse:
            # Перед кликом убедимся, что кнопка готова
            self.search_button.wait_for(state="visible")
            self.search_button.click()
        else:
            self.search_input.press("Enter")

    def open_catalog(self) -> None:
        """
        Нажимает на кнопку каталога для открытия выпадающего меню.
        """
        self.catalog_button.wait_for(state="visible")
        self.catalog_button.click()