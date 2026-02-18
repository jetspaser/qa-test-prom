

"""
Тесты функциональности поиска на сайте promminer.ru.
"""
import re
from playwright.sync_api import Page, expect
from pages.header import Header


class TestSearch:
    """
    Класс для проверки поиска.
    """

    def test_search_s23_positive(self, page: Page):
        """
        Положительный тест: поиск существующего товара 's23' через Enter.
        """
        header = Header(page)
        header.open("https://promminer.ru")
        header.search("s23")

        # Проверка H1 (Главный заголовок страницы результатов)
        expect(page.locator("h1")).to_contain_text("поиск", ignore_case=True)

        # Проверка наличия карточек товаров
        product_card = page.locator(".catalog-block__item").first
        expect(product_card).to_be_visible(timeout=10000)

    def test_search_s23_with_click(self, page: Page):
        """
        Демонстрация лайв-кодинга: поиск через клик по лупе.
        """
        header = Header(page)
        header.open("https://promminer.ru")

        # Теперь клик не упадет из-за дубликатов, так как локатор уточнен
        header.search("s23", use_mouse=True)

        # Проверка H1 (Главный заголовок страницы результатов)
        expect(page.locator("h1")).to_contain_text("поиск", ignore_case=True)

        # Проверка наличия карточек товаров
        product_card = page.locator(".catalog-block__item").first
        expect(product_card).to_be_visible(timeout=10000)

    def test_search_s23_buy_bug(self, page):
        header = Header(page)
        header.open("https://promminer.ru")
        header.search("s23 найти")

        # Проверяем текст ошибки
        not_found_text = page.get_by_text("Сожалеем, но ничего не найдено")

        # В этом тесте мы ЖДЕМ падения, если баг есть.
        # Если текст виден — expect упадет, и это зафиксирует баг.
        expect(not_found_text).not_to_be_visible(timeout=5000)

        # Проверяем, что карточки товаров всё-таки есть
        expect(page.locator(".catalog-block__item").first).to_be_visible()
