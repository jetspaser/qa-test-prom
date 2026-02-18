

"""
Модуль с описанием контента главной страницы (Main Page).
"""
# Импортируем классы Page (браузер) и Locator (ссылка на элемент) для типизации
from playwright.sync_api import Page, Locator
# Импортируем базовый класс. Из него мы наследуем общие методы (например, open)
from .base_page import BasePage

class MainPage(BasePage):
    """
    Класс для взаимодействия с уникальными блоками главной страницы.
    """

    def __init__(self, page: Page):
        """
        Инициализация локаторов основного блока.
        :param page: Объект страницы Playwright.
        """
        # Вызываем конструктор родительского класса BasePage, чтобы пробросить туда объект page
        super().__init__(page)

        # --- ЛОКАТОРЫ ---
        # Мы не ищем элементы в момент создания объекта, а просто создаем "ярлыки" (Locators).
        # Playwright найдет их физически только в момент действия (click, visible и т.д.)

        # Поиск по CSS-селектору:
        # a.btn -> ищем тег 'a' (ссылка) с классом 'btn'
        # [href="..."] -> фильтруем, чтобы атрибут href был именно таким
        # .first -> берем первую подходящую кнопку (чтобы не зацепить такие же в меню)
        self.asic_miners_card: Locator = page.locator('a.btn[href="/product/asic-miners/"]').first

        # Поиск по тексту (get_by_text):
        # Ищет элемент, внутри которого есть эта фраза. Очень удобно для проверки контента.
        self.support_info_text: Locator = page.get_by_text(
            "Полное сопровождение — от закупки оборудования до подключения к пулу"
        )

        # exact=True заставляет Playwright искать строгое совпадение.
        # Если на странице будет "Майнинг под ключ 2.0", этот локатор его проигнорирует.
        self.mining_turnkey_banner: Locator = page.get_by_text("Майнинг под ключ", exact=True)

    # --- МЕТОДЫ (ДЕЙСТВИЯ) ---

    def click_asic_miners_category(self) -> None:
        """
        Переход в раздел Asic майнеров через плитку на главной странице.
        """
        # wait_for(state="visible") — принудительно ждем, пока элемент не просто появится в коде,
        # а станет видимым глазу (отрисуется, закончатся анимации).
        self.asic_miners_card.wait_for(state="visible")

        # Выполняем клик. Playwright автоматически прокрутит страницу к элементу перед кликом.
        self.asic_miners_card.click()

    def scroll_to_support_info(self) -> None:
        """
        Прокручивает страницу до блока с текстом о сопровождении.
        """
        # scroll_into_view_if_needed — полезная штука. Она плавно скроллит страницу так,
        # чтобы нужный элемент оказался в зоне видимости (Viewport).
        # Если элемент уже виден, функция ничего не будет делать.
        self.support_info_text.scroll_into_view_if_needed()
