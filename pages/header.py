

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

        # Поле ввода поиска (ID стабилен)
        self.search_input: Locator = page.locator("#title-search-input")

        # РЕШЕНИЕ: Уточняем, что нам нужен каталог именно внутри тега <header>
        # и берем первый подходящий (обычно это десктопная версия)
        self.catalog_button: Locator = page.locator("header").get_by_text("Каталог", exact=True).first

        # Ссылка на Telegram в верхней части
        self.telegram_icon: Locator = page.locator("header a[href*='t.me']")

        # Кнопка "Заказать звонок"
        self.callback_button: Locator = page.locator("header").get_by_text("Заказать звонок")

    def search(self, text: str) -> None:
        """
        Выполняет поиск товара через ввод текста и нажатие клавиши Enter.
        :param text: Текст поискового запроса.
        """
        self.search_input.fill(text)
        self.search_input.press("Enter")

    def open_catalog(self) -> None:
        """
        Нажимает на кнопку каталога для открытия выпадающего меню.
        """
        self.catalog_button.click()




    # def __init__(self, page: Page):
    #     """
    #     Инициализация локаторов шапки.
    #     """
    #     super().__init__(page)
    #     # Поле ввода поиска (ID уникален для главной страницы)
    #     self.search_input = page.locator("#title-search-input")
    #     # Локатор для блока с описанием сопровождения
    #     self.support_text = page.locator("text=Полное сопровождение — от закупки оборудования")
    #     # Кнопка Asic майнеры (ищем по тексту)
    #     self.asic_miners_btn = page.locator("a", has_text="Asic майнеры").first
    #
    #     # ЛОКАТОР КНОПКИ (закомментирован как доп. вариант)
    #     # На сайте promminer.ru кнопка поиска обычно имеет атрибут name='s' или класс 'search-btn'
    #     # self.search_button = page.locator("button[name='s']")


    # def search(self, text: str):
    #     """
    #     Выполняет поиск товара.
    #
    #     :param text: Текст поискового запроса.
    #     """
    #     # 1. Заполняем поле текстом
    #     self.search_input.fill(text)
    #
    #     # 2. ОСНОВНОЙ ВАРИАНТ: Нажимаем Enter (универсально для десктопа и адаптива)
    #     self.search_input.press("Enter")
    #
    #     # ---------------------------------------------------------
    #     # ДОПОЛНИТЕЛЬНЫЙ ВАРИАНТ (через клик по лупе):
    #     # Чтобы использовать его, закомментируй строку выше и раскомментируй это:
    #     # if self.search_button.is_visible():
    #     #     self.search_button.click()
    #     # else:
    #     #     self.search_input.press("Enter")
    #     # ---------------------------------------------------------