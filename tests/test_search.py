"""
Тесты функциональности поиска на сайте promminer.ru.
"""
# import re
from playwright.sync_api import expect
from pages.header import Header


class TestSearch:
    """
    Класс для проверки поиска. Мы используем реальные локаторы сайта promminer.ru.
    """

    def test_search_s23_positive(self, page):
        header = Header(page)
        header.open("https://promminer.ru")
        header.search("s23")

        # Проверяем заголовок
        expect(page.locator("h1")).to_contain_text("поиск", ignore_case=True)
    #
    #     # Используем класс, который мы нашли в твоем HTML
    #     # Добавляем видимую проверку для ПЕРВОГО элемента
    #     product_card = page.locator(".catalog-block__item").first
    #
    #     # Ждем, чтобы элемент не просто был в коде, а стал видимым (отрисованным)
    #     expect(product_card).to_be_visible(timeout=10000)
    #
    # def test_search_s23_buy_bug(self, page):
    #     header = Header(page)
    #     header.open("https://promminer.ru")
    #     header.search("s23 найти")
    #
    #     # Проверяем текст ошибки
    #     not_found_text = page.get_by_text("Сожалеем, но ничего не найдено")
    #
    #     # В этом тесте мы ЖДЕМ падения, если баг есть.
    #     # Если текст виден — expect упадет, и это зафиксирует баг.
    #     expect(not_found_text).not_to_be_visible(timeout=5000)
    #
    #     # Проверяем, что карточки товаров всё-таки есть
    #     expect(page.locator(".catalog-block__item").first).to_be_visible()