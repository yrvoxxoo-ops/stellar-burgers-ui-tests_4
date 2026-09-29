import allure
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from pages.locators import FeedPageLocators
from urls import FEED_URL


class FeedPage(BasePage):

    @allure.step("Открываем страницу ленты заказов")
    def open_feed_page(self):
        self.open_page(FEED_URL)

    @allure.step("Получаем заголовок ленты заказов")
    def get_order_feed_title(self):
        return self.get_text(FeedPageLocators.ORDER_FEED_TITLE)

    @allure.step("Получаем значение счётчика Выполнено за всё время")
    def get_total_counter_value(self):
        counter_text = self.get_text(FeedPageLocators.TOTAL_COUNTER)
        return int(counter_text.replace(" ", ""))

    @allure.step("Получаем значение счётчика Выполнено за сегодня")
    def get_today_counter_value(self):
        counter_text = self.get_text(FeedPageLocators.TODAY_COUNTER)
        return int(counter_text.replace(" ", ""))

    @allure.step("Получаем список заказов в работе")
    def get_orders_in_progress_text(self):
        return self.get_text(FeedPageLocators.ORDERS_IN_PROGRESS)

    @allure.step("Проверяем, что номер заказа отображается в разделе В работе")
    def is_order_number_in_progress(self, order_number):
        clean_order_number = order_number.replace("#", "").strip()

        def order_number_is_visible_in_progress(driver):
            orders_in_progress_text = self.get_orders_in_progress_text()
            return clean_order_number in orders_in_progress_text

        return WebDriverWait(self.driver, 30).until(order_number_is_visible_in_progress)
    @allure.step("Ждём увеличения счётчика Выполнено за всё время")
    def wait_until_total_counter_increased(self, old_value):
        def total_counter_is_increased(driver):
            new_value = self.get_total_counter_value()

            if new_value > old_value:
                return new_value

            return False

        return WebDriverWait(self.driver, 60).until(total_counter_is_increased)

    @allure.step("Ждём увеличения счётчика Выполнено за сегодня")
    def wait_until_today_counter_increased(self, old_value):
        def today_counter_is_increased(driver):
            new_value = self.get_today_counter_value()

            if new_value > old_value:
                return new_value

            return False

        return WebDriverWait(self.driver, 60).until(today_counter_is_increased)