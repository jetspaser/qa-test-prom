"""
Комплексные тесты для проверки подвала (Footer) сайта promminer.ru.
"""
from playwright.sync_api import Page, expect
from pages.footer import Footer

class TestFooter:
    """
    Набор тестов для верификации элементов футера.
    """

    def test_footer_service_text_visibility(self, page: Page) -> None:
        """
        Тест №1: Проверка наличия текста 'Сервис' в футере.

        :param page: Объект страницы Playwright.
        """
        footer = Footer(page)
        footer.open("https://promminer.ru")

        # Прокрутка вниз для гарантии видимости футера
        page.keyboard.press("End")
        page.wait_for_timeout(500)

        # Проверяем, что ссылка с текстом "Сервис" видна на странице
        expect(footer.service_link_text).to_be_visible(timeout=5000)

        # Дополнительно проверяем корректность атрибута href
        expect(footer.service_link_text).to_have_attribute("href", "/service_support/")

    def test_footer_telegram_click(self, page: Page) -> None:
        """
        Тест №2: Клик по ссылке на соцсеть Telegram.

        :param page: Объект страницы Playwright.
        """
        footer = Footer(page)
        footer.open("https://promminer.ru")

        # Используем метод Page Object для клика
        # Playwright автоматически обработает открытие новой вкладки (target="_blank")
        footer.click_telegram_social()

        # Проверяем, что ссылка в объекте содержит базовый домен telegram
        # (не проверяем весь UTM-хвост, так как он может меняться)
        tg_href = footer.tg_social_link.get_attribute("href")
        assert "t.me/promminer" in tg_href, f"Неверная ссылка в соцсетях: {tg_href}"