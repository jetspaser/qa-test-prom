

"""
Комплексные тесты главной страницы: проверка контента, навигации и футера.
"""
# Импортируем модуль регулярных выражений для гибкой проверки текстов/URL
import re

# Импортируем типы для подсказок IDE и функцию expect (главный инструмент проверок)
from playwright.sync_api import Page, expect

# Импортируем наши Page Objects (описания страниц)
from pages.main_page import MainPage
from pages.footer import Footer
from pages.header import Header


class TestMainPage:
    """
    Класс тестов для проверки сквозных элементов и главной страницы.
    """

    def test_main_page_content_integrity(self, page: Page):
        # Создаем экземпляр страницы, передавая туда драйвер 'page'
        main_page = MainPage(page)

        # Вызываем метод открытия URL (прописан в базовом классе или MainPage)
        main_page.open("https://promminer.ru")

        # Проверка: ожидаем, что локатор текста на странице станет видимым
        # expect — это ассерция (утверждение). Если условие не выполнится, тест упадет тут.
        expect(main_page.support_info_text).to_be_visible()

        # Вызываем логику клика по плитке (внутри метода зашито ожидание и сам клик)
        main_page.click_asic_miners_category()

        # expect(page).to_have_url — проверяет текущий адрес браузера
        # re.compile — создает шаблон. Мы проверяем, что URL содержит нужный путь,
        # игнорируя то, что может быть до или после (например, параметры метрик)
        expect(page).to_have_url(re.compile(r".*/product/asic-miners/"))

    def test_footer_contacts_and_socials(self, page: Page):
        # Инициализируем объект футера
        footer = Footer(page)
        footer.open("https://promminer.ru")

        # ИСПРАВЛЕНО: используем tg_social_link вместо tg_link
        expect(footer.tg_social_link).to_be_visible()

    def test_header_catalog_presence(self, page: Page):
        header = Header(page)
        header.open("https://promminer.ru")

        # Проверяем кнопку "Каталог" в шапке
        expect(header.catalog_button).to_be_visible()

    def test_header_catalog_navigation(self, page: Page):
        header = Header(page)
        header.open("https://promminer.ru")

        # 1. Выполняем метод открытия меню (клик по кнопке "Каталог")
        header.open_catalog()

        # 2. Искусственная пауза (1000 мс = 1 сек).
        # Нужна, так как меню на сайте вылетает с плавной анимацией, и Playwright
        # может попытаться кликнуть, пока элемент еще "движется" или наполовину прозрачен.
        page.wait_for_timeout(1000)

        # 3. Сложный локатор:
        # .locator(".header-menu__wide-submenu a") — ищем все ссылки 'a' внутри блока меню.
        # .get_by_text("Whatsminer", exact=True) — фильтруем, чтобы найти только текст "Whatsminer".
        # .first — берем первый найденный элемент (если их вдруг несколько в верстке).
        catalog_item = page.locator(".header-menu__wide-submenu a").get_by_text("Whatsminer", exact=True).first

        # Проверяем видимость с запасом по времени (timeout 10 сек)
        expect(catalog_item).to_be_visible(timeout=10000)

        # 4. Конструктор 'with page.expect_navigation'
        # Это "ловушка" для перехода. Мы говорим: "Сейчас внутри этого блока произойдет клик,
        # и ты, Playwright, не иди к следующей строке кода, пока страница не обновится".
        # wait_until="networkidle" — ждать, пока в течение 500мс не будет новых запросов по сети.
        with page.expect_navigation(wait_until="networkidle"):
            # force=True — кликнуть в любом случае, даже если Playwright считает,
            # что элемент перекрыт другим (актуально для анимированных меню).
            catalog_item.click(force=True)

        # 5. Финальная проверка: убеждаемся, что мы на странице бренда Whatsminer
        expect(page).to_have_url(re.compile(r".*/whatsminer/.*"))
