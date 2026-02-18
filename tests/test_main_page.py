

"""
Комплексные тесты главной страницы: проверка контента, навигации и футера.
"""
import re
from playwright.sync_api import Page, expect
from pages.main_page import MainPage
from pages.footer import Footer
from pages.header import Header


class TestMainPage:
    """
    Класс тестов для проверки сквозных элементов и главной страницы.
    """

    def test_main_page_content_integrity(self, page: Page):
        """
        Тест проверяет наличие ключевого текста на главной и работу ссылки в категорию.
        """
        main_page = MainPage(page)

        # 1. Открываем главную страницу
        main_page.open("https://promminer.ru")

        # 2. Проверяем наличие блока с описанием услуг
        # Playwright сам подождет появления текста (Auto-waiting)
        expect(main_page.support_info_text).to_be_visible()

        # 3. Кликаем по категории в основном блоке
        main_page.click_asic_miners_category()

        # 4. Проверяем, что URL сменился на раздел асиков
        expect(page).to_have_url(re.compile(r".*/asic-maynery/.*"))

    def test_footer_contacts_and_socials(self, page: Page):
        """
        Тест проверяет элементы футера: Telegram и Политику конфиденциальности.
        """
        footer = Footer(page)

        # Открываем страницу (можно любую, так как футер везде один)
        footer.open("https://promminer.ru")

        # Проверяем видимость ссылки на Telegram
        expect(footer.tg_link).to_be_visible()

        # Проверяем наличие ссылки на юридическую информацию
        expect(footer.privacy_policy_link).to_be_visible()

    def test_header_catalog_presence(self, page: Page):

        """
        Проверка видимости кнопки каталога через Page Object.
        """

        header = Header(page)

        header.open("https://promminer.ru")

        # Используем локатор прямо из объекта хедера
        expect(header.catalog_button).to_be_visible()

    def test_header_catalog_navigation(self, page: Page):
        header = Header(page)
        header.open("https://promminer.ru")

        # Кликаем по каталогу
        header.open_catalog()

        # Ждем появления элемента меню. Используем более общий селектор.
        # На этом сайте выпадающее меню часто имеет класс .menu-navigation или просто доступно по тексту
        catalog_item = page.locator(".header-menu__wide-submenu").get_by_text("MicroBT Whatsminer").first

        # Если не находит, попробуй форсировать ожидание именно видимого элемента
        expect(catalog_item).to_be_visible(timeout=10000)

        # 4. Выбираем категорию (например, MicroBT Whatsminer)
        # Можно сделать через универсальный локатор по тексту внутри меню
        whatsminer_category = page.locator(".menu-navigation__item-link", has_text="MicroBT Whatsminer")

        # Прокрутим к ней, если меню длинное, и кликнем
        whatsminer_category.scroll_into_view_if_needed()
        whatsminer_category.click()

        # 5. Проверяем, что URL изменился на страницу категории
        expect(page).to_have_url(re.compile(r".*/product/microbt/.*"))