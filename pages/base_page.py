

"""
BasePage.

Базовый класс для всех Page Object.
Содержит общие методы взаимодействия со страницей,
такие как клик, ввод текста и ожидания элементов.
"""

from playwright.sync_api import Page, Locator


class BasePage:
    """
    Базовый Page Object.

    Содержит общие методы для работы со страницей:
    переходы, клики, ввод данных и ожидания элементов.
    """

    def __init__(self, page: Page) -> None:
        """
        Инициализация базовой страницы.

        :param page: Экземпляр страницы Playwright
        """
        self.page = page

    def open(self, url: str) -> None:
        """
        Открыть страницу по указанному URL.

        :param url: URL страницы
        """
        self.page.goto(url)

    def click(self, locator: Locator) -> None:
        """
        Выполнить клик по элементу.

        :param locator: Локатор элемента
        """
        locator.click()

    def fill(self, locator: Locator, text: str) -> None:
        """
        Ввести текст в поле ввода.

        :param locator: Локатор поля ввода
        :param text: Текст для ввода
        """
        locator.fill(text)

    def get_text(self, locator: Locator) -> str:
        """
        Получить текст элемента.

        :param locator: Локатор элемента
        :return: Текст элемента
        """
        return locator.text_content()

    def is_visible(self, locator: Locator) -> bool:
        """
        Проверить, отображается ли элемент на странице.

        :param locator: Локатор элемента
        :return: True, если элемент видим
        """
        return locator.is_visible()

    def wait_for_visible(self, locator: Locator, timeout: int = 5000) -> None:
        """
        Ожидать появления элемента на странице.

        :param locator: Локатор элемента
        :param timeout: Таймаут ожидания в миллисекундах
        """
        locator.wait_for(state="visible", timeout=timeout)

