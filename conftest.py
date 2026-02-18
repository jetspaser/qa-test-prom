

import pytest
from playwright.sync_api import Browser, BrowserContext

@pytest.fixture(scope="session", autouse=True)
def set_data_test_attribute(playwright):
    """
    Устанавливает кастомный data-атрибут для всех тестов.
    Позволяет использовать page.get_by_test_id("some-id") для атрибутов data-test.
    """
    playwright.selectors.set_test_id_attribute("data-test")

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """
    Глобальная настройка контекста браузера.
    Здесь мы задаем размер окна и базовый URL.
    """
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "base_url": "https://promminer.ru"
    }

@pytest.fixture(scope="function")
def page(context: BrowserContext):
    """
    Опционально: фикстура для расширенной настройки страницы,
    например, для автоматического создания скриншотов при падении.
    """
    page = context.new_page()
    yield page
    # Здесь можно добавить логику закрытия или сохранения логов
