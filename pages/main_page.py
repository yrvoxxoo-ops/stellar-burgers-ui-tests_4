import allure

from pages.base_page import BasePage
from pages.locators import HeaderLocators, MainPageLocators
from urls import BASE_URL
from selenium.webdriver.support.ui import WebDriverWait

class MainPage(BasePage):

    @allure.step("Открываем главную страницу")
    def open_main_page(self):
        self.open_page(BASE_URL)

    @allure.step("Переходим в конструктор")
    def click_constructor_link(self):
        self.click_element(HeaderLocators.CONSTRUCTOR_LINK)

    @allure.step("Переходим в ленту заказов")
    def click_order_feed_link(self):
        self.click_element(HeaderLocators.ORDER_FEED_LINK)

    @allure.step("Переходим в личный кабинет")
    def click_personal_account_link(self):
        self.click_element(HeaderLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step("Кликаем по кнопке Войти в аккаунт")
    def click_login_to_account_button(self):
        self.click_element(MainPageLocators.LOGIN_TO_ACCOUNT_BUTTON)

    @allure.step("Получаем заголовок конструктора")
    def get_constructor_title(self):
        return self.get_text(MainPageLocators.CONSTRUCTOR_TITLE)

    @allure.step("Кликаем по первой булке")
    def click_first_bun(self):
        self.click_element(MainPageLocators.FIRST_BUN)

    @allure.step("Проверяем, что модальное окно ингредиента отображается")
    def is_ingredient_modal_visible(self):
        return self.is_element_visible(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step("Закрываем модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click_element(MainPageLocators.INGREDIENT_MODAL_CLOSE_BUTTON)

    @allure.step("Получаем значение счётчика первой булки")
    def get_first_bun_counter_value(self):
        return int(self.get_text(MainPageLocators.FIRST_BUN_COUNTER))

    @allure.step("Добавляем булку в заказ")
    def add_bun_to_order(self):
        self.drag_and_drop(MainPageLocators.FIRST_BUN, MainPageLocators.TOP_BUN_DROP_AREA)

    @allure.step("Добавляем соус в заказ")
    def add_sauce_to_order(self):
        self.drag_and_drop(MainPageLocators.FIRST_SAUCE, MainPageLocators.INGREDIENT_DROP_AREA)

    @allure.step("Добавляем начинку в заказ")
    def add_filling_to_order(self):
        self.drag_and_drop(
            MainPageLocators.FIRST_FILLING,
            MainPageLocators.INGREDIENT_DROP_AREA
        )

    @allure.step("Нажимаем кнопку Оформить заказ")
    def click_create_order_button(self):
        self.click_element(MainPageLocators.CREATE_ORDER_BUTTON)

    @allure.step("Получаем номер заказа из модального окна")
    def get_order_number_from_modal(self):
        def order_number_is_loaded(driver):
            order_number = self.get_text(MainPageLocators.ORDER_NUMBER_IN_MODAL).replace("#", "").strip()
            if order_number.isdigit() and order_number != "9999":
                return order_number
            return False
        return WebDriverWait(self.driver, 60).until(order_number_is_loaded)

    @allure.step("Закрываем модальное окно заказа")
    def close_order_modal(self):
        self.click_element(MainPageLocators.ORDER_MODAL_CLOSE_BUTTON)
    
    @allure.step("Проверяем, что модальное окно ингредиента закрылось")
    def is_ingredient_modal_closed(self):
        return self.wait_until_element_is_not_visible(MainPageLocators.INGREDIENT_MODAL_TITLE)
    
    @allure.step("Создаём заказ")
    def create_order(self):
        self.add_bun_to_order()
        self.add_sauce_to_order()
        self.add_filling_to_order()
        self.click_create_order_button()