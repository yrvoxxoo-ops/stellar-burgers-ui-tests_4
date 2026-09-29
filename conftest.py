import uuid
import allure
import pytest
from pages.locators import MainPageLocators
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from data import BrowserName, UserData
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage
from urls import LOGIN_URL


@pytest.fixture(params=[BrowserName.CHROME, BrowserName.FIREFOX])
def driver(request):
    browser_name = request.param
    allure.dynamic.parameter("browser", browser_name)
    if browser_name == BrowserName.CHROME:
        options = ChromeOptions()
        options.page_load_strategy = "eager"
        driver = webdriver.Chrome(options=options)
    elif browser_name == BrowserName.FIREFOX:
        options = FirefoxOptions()
        options.page_load_strategy = "eager"
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")
    driver.maximize_window()
    driver.set_page_load_timeout(120)
    yield driver
    driver.quit()


@pytest.fixture
def user_data():
    unique_part = uuid.uuid4().hex
    return {"name": f"User_{unique_part}", "email": f"test_user_{unique_part}@yandex.ru", "password": UserData.PASSWORD}

@pytest.fixture
def registered_user(driver, user_data):
    register_page = RegisterPage(driver)
    with allure.step("Открываем страницу регистрации"):
        register_page.open_register_page()
    with allure.step("Регистрируем нового пользователя через UI"):
        register_page.register_user(user_data["name"], user_data["email"], user_data["password"])
    with allure.step("Ждём переход на страницу авторизации после регистрации"):
        register_page.wait_until_url_contains("/login")
    return user_data


@pytest.fixture
def logged_in_user(driver, registered_user):
    login_page = LoginPage(driver)
    main_page = MainPage(driver)
    with allure.step("Открываем страницу авторизации"):
        login_page.open_page(LOGIN_URL)
    with allure.step("Авторизуемся зарегистрированным пользователем через UI"):
        login_page.login(registered_user["email"], registered_user["password"])
    with allure.step("Ждём переход на главную страницу после авторизации"):
        main_page.find_visible_element(MainPageLocators.CONSTRUCTOR_TITLE)
    return registered_user