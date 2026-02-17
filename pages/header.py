

"""
Page Object хедера сайта.
"""


from playwright.sync_api import Page, Locator


class Header:
    """
    Header.

    Содержит элементы навигации,
    поиска и внешних ссылок.
    """

    def __init__(self, page: Page) -> None:
        """
        Инициализация хедера.

        :param page: Экземпляр страницы Playwright
        """
        self.page = page

        # Локаторы хедера
        self.search_input: Locator = page.get_by_placeholder("поиск")
        self.telegram_link: Locator = page.get_by_role("link", name="Telegram")
        self.catalog_link: Locator = page.get_by_role("link", name="Каталог")

    def search(self, text: str) -> None:
        """
        Выполнить поиск по заданному тексту.

        :param text: Текст для поиска
        """
        self.search_input.fill(text)
        self.search_input.press("Enter")

    def open_catalog(self) -> None:
        """
        Открыть страницу каталога через хедер.
        """
        self.catalog_link.click()

    def open_telegram(self) -> None:
        """
        Перейти по ссылке на Telegram.
        """
        self.telegram_link.click()
