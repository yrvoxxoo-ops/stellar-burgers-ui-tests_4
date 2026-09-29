import allure

from pages.base_page import BasePage
from pages.locators import LoginPageLocators
from urls import LOGIN_URL


class LoginPage(BasePage):

    @allure.step("Открываем страницу авторизации")
    def open_login_page(self):
        self.open_page(LOGIN_URL)

    @allure.step("Вводим email")
    def set_email(self, email):
        self.set_text(LoginPageLocators.EMAIL_INPUT, email)

    @allure.step("Вводим пароль")
    def set_password(self, password):
        self.set_text(LoginPageLocators.PASSWORD_INPUT, password)

    @allure.step("Кликаем по кнопке Войти")
    def click_login_button(self):
        self.click_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step("Авторизуемся")
    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

    @allure.step("Переходим на страницу регистрации")
    def click_register_link(self):
        self.click_element(LoginPageLocators.REGISTER_LINK)