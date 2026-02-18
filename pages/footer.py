

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
        """
        super().__init__(page)
        # Ссылка на Telegram в футере (используем селектор по атрибуту href)
        self.tg_link: Locator = page.locator("footer a[href*='t.me/promminer']")
        # Ссылка на политику конфиденциальности
        self.privacy_policy_link: Locator = page.locator("footer a", has_text="Политика конфиденциальности")
        # Текст с копирайтом или адресом
        self.address_info: Locator = page.locator("footer .contact-block")

    def click_telegram(self):
        """
        Переходит по ссылке в Telegram.
        """
        self.tg_link.click()