

"""
Базовый класс для всех страниц.
Содержит общие методы и инициализацию драйвера.
"""

# Импортируем класс Page из библиотеки Playwright.
# Это нужно для "тайп-хинтинга" (подсказок), чтобы IDE понимала, что self.page — это браузер.
from playwright.sync_api import Page


class BasePage:
    """
    Класс-родитель, от которого наследуются все Page Objects.
    """

    def __init__(self, page: Page):
        """
        Конструктор класса.
        :param page: Передает объект страницы Playwright (текущую вкладку браузера).
        """
        # Сохраняем переданный объект page внутри класса.
        # Теперь во всех дочерних классах (через self.page) мы сможем кликать и искать элементы.
        self.page = page

    def open(self, url: str):
        """
        Универсальный метод для открытия любого URL.
        :param url: Полный адрес страницы (например, https://promminer.ru).
        """
        # Метод .goto() — это встроенная команда Playwright для перехода по адресу.
        # Мы вынесли её сюда, чтобы не писать self.page.goto в каждом тесте.
        self.page.goto(url)



# На перспективу код (разбор playwright)
#
# """
# Модуль содержит базовый класс для всех Page Objects.
# Здесь описываются общие методы, не привязанные к конкретным элементам.
# """
#
# from playwright.sync_api import Page, Response, expect
# from typing import Optional
#
#
# class BasePage:
#     """
#     Базовый класс страницы.
#
#     Почему мы не оборачиваем click() и fill():
#     Playwright реализует Auto-waiting "из коробки". Создание методов-оберток
#     скрывает нативную трассировку ошибок и избыточно для этого фреймворка.
#     """
#
#     def __init__(self, page: Page):
#         """
#         Инициализация базового класса.
#         :param page: Объект страницы Playwright.
#         """
#         self.page = page
#
#     def open(self, url: str) -> Optional[Response]:
#         """
#         По умолчанию Playwright ждет события load
#         (когда загрузится всё, включая тяжелые скрипты аналитики и картинки)
#         """
#         return self.page.goto(url, wait_until="domcontentloaded")
#
#     def verify_url(self, expected_url_part: str):
#         """
#         Проверяет, что текущий URL содержит ожидаемую подстроку.
#         Используем Web-First assertion для автоматического ожидания.
#         """
#         expect(self.page).to_have_url(expected_url_part)
#
#     def get_page_title(self) -> str:
#         """Возвращает заголовок вкладки браузера."""
#         return self.page.title()
#
#     def reload(self):
#         """Перезагружает текущую страницу."""
#         self.page.reload(wait_until="domcontentloaded")

