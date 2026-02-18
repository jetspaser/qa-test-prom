

"""
Модуль с описанием контента главной страницы (Main Page).
"""
from playwright.sync_api import Page, Locator
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
        super().__init__(page)

        # Большие плитки категорий (Asic майнеры, Дата-центр и т.д.)
        self.asic_miners_card = page.locator("#content a").filter(has_text="Asic майнеры").first
        self.data_center_card: Locator = page.locator("a").filter(has_text="Дата-центр").first

        # Информационный текст (на твоем скриншоте — внизу слева)
        self.support_info_text: Locator = page.get_by_text(
            "Полное сопровождение — от закупки оборудования до подключения к пулу"
        )
        self.asic_miners_card: Locator = page.locator(".sections-main").get_by_text("Asic майнеры").first

        # Блок "Майнинг под ключ" (большая синяя/темная плашка)
        self.mining_turnkey_banner: Locator = page.get_by_text("Майнинг под ключ", exact=True)

    def click_asic_miners_category(self) -> None:
        """
        Переход в раздел Asic майнеров через плитку на главной странице.
        """
        self.asic_miners_card.click()

    def scroll_to_support_info(self) -> None:
        """
        Прокручивает страницу до блока с текстом о сопровождении.
        """
        self.support_text.scroll_into_view_if_needed()