import allure

from pages.base_page import BasePage
from pages.locators import RegisterPageLocators
from urls import REGISTER_URL


class RegisterPage(BasePage):

    @allure.step("Открываем страницу регистрации")
    def open_register_page(self):
        self.open_page(REGISTER_URL)

    @allure.step("Вводим имя пользователя")
    def set_name(self, name):
        self.set_text(RegisterPageLocators.NAME_INPUT, name)

    @allure.step("Вводим email пользователя")
    def set_email(self, email):
        self.set_text(RegisterPageLocators.EMAIL_INPUT, email)

    @allure.step("Вводим пароль пользователя")
    def set_password(self, password):
        self.set_text(RegisterPageLocators.PASSWORD_INPUT, password)

    @allure.step("Кликаем по кнопке Зарегистрироваться")
    def click_register_button(self):
        self.click_element(RegisterPageLocators.REGISTER_BUTTON)

    @allure.step("Регистрируем нового пользователя")
    def register_user(self, name, email, password):
        self.set_name(name)
        self.set_email(email)
        self.set_password(password)
        self.click_register_button()

    @allure.step("Переходим на страницу авторизации")
    def click_login_link(self):
        self.click_element(RegisterPageLocators.LOGIN_LINK)