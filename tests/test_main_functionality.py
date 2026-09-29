import allure

from data import Text
from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.feature("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Переход по клику на Конструктор")
    @allure.story("Навигация")
    def test_click_constructor_opens_constructor_page(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        with allure.step("Открываем ленту заказов"):
            feed_page.open_feed_page()
        with allure.step("Кликаем на Конструктор"):
            main_page.click_constructor_link()
        with allure.step("Проверяем, что открылась страница конструктора"):
            assert main_page.get_constructor_title() == Text.CONSTRUCTOR_TITLE

    @allure.title("Переход по клику на Лента заказов")
    @allure.story("Навигация")
    def test_click_order_feed_opens_order_feed_page(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)
        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()
        with allure.step("Кликаем на Лента заказов"):
            main_page.click_order_feed_link()
        with allure.step("Проверяем, что открылась лента заказов"):
            assert feed_page.get_order_feed_title() == Text.ORDER_FEED_TITLE

    @allure.title("Открытие всплывающего окна с деталями ингредиента")
    @allure.story("Модальное окно ингредиента")
    def test_click_ingredient_opens_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()
        with allure.step("Кликаем по ингредиенту"):
            main_page.click_first_bun()
        with allure.step("Проверяем, что открылось модальное окно с деталями ингредиента"):
            assert main_page.is_ingredient_modal_visible()

    @allure.title("Закрытие всплывающего окна ингредиента по крестику")
    @allure.story("Модальное окно ингредиента")
    def test_click_close_button_closes_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()
        with allure.step("Открываем модальное окно ингредиента"):
            main_page.click_first_bun()
        with allure.step("Закрываем модальное окно"):
            main_page.close_ingredient_modal()
        with allure.step("Проверяем, что модальное окно закрылось"):
            assert main_page.is_ingredient_modal_closed()

    @allure.title("Увеличение счётчика ингредиента при добавлении в заказ")
    @allure.story("Конструктор заказа")
    def test_add_ingredient_to_order_increases_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        with allure.step("Открываем главную страницу"):
            main_page.open_main_page()
        with allure.step("Получаем значение счётчика ингредиента до добавления"):
            counter_before = main_page.get_first_bun_counter_value()
        with allure.step("Добавляем булку в заказ"):
            main_page.add_bun_to_order()
        with allure.step("Получаем значение счётчика ингредиента после добавления"):
            counter_after = main_page.get_first_bun_counter_value()
        with allure.step("Проверяем, что счётчик увеличился"):
            assert counter_after > counter_before