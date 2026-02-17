

"""
Тесты поиска на сайте promminer.ru
"""

from pages.header import Header


def test_search_s19(page):
    """
    Проверка поиска по запросу 's19'.

    Шаги:
    1. Открыть главную страницу
    2. Ввести 's19' в поиск
    3. Убедиться, что страница с результатами открылась
    """

    page.goto("https://promminer.ru")

    header = Header(page)
    header.search("s19")

    # Минимальная, но валидная проверка
    assert "s19" in page.url.lower()
