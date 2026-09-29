from selenium.webdriver.common.by import By


class HeaderLocators:
    CONSTRUCTOR_LINK = (By.XPATH, "//p[contains(normalize-space(.), 'Конструктор')]/ancestor::a")

    ORDER_FEED_LINK = (By.XPATH, "//p[contains(normalize-space(.), 'Лента Заказов') or contains(normalize-space(.), 'Лента заказов')]/ancestor::a")

    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[contains(normalize-space(.), 'Личный Кабинет') or contains(normalize-space(.), 'Личный кабинет')]/ancestor::a")

class MainPageLocators:
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[contains(normalize-space(.), 'Соберите бургер')]")
    LOGIN_TO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(normalize-space(.), 'Войти в аккаунт')]")
    BUN_SECTION = (By.XPATH, "//h2[contains(normalize-space(.), 'Булки')]")
    SAUCE_SECTION = (By.XPATH, "//h2[contains(normalize-space(.), 'Соусы')]")
    FILLING_SECTION = (By.XPATH, "//h2[contains(normalize-space(.), 'Начинки')]")
    FIRST_BUN = (By.XPATH, "//a[contains(@href, '/ingredient/') and .//p[contains(normalize-space(.), 'Флюоресцентная булка R2-D3')]]")

    FIRST_BUN_COUNTER = (By.XPATH,"//a[contains(@href, '/ingredient/') and .//p[contains(normalize-space(.), 'Флюоресцентная булка R2-D3')]]"
        "//*[contains(@class, 'counter_counter__num')]")

    FIRST_SAUCE = (By.XPATH,"//a[contains(@href, '/ingredient/') and .//p[contains(normalize-space(.), 'Соус Spicy-X')]]")
    FIRST_FILLING = (By.XPATH,"//a[contains(@href, '/ingredient/') and .//p[contains(normalize-space(.), 'Мясо бессмертных моллюсков Protostomia')]]")

    INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[contains(normalize-space(.), 'Детали ингредиента')]")
    INGREDIENT_MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

    TOP_BUN_DROP_AREA = (By.XPATH, "//span[contains(normalize-space(.), 'Перетяните булочку сюда (верх)')]/ancestor::li")

    BOTTOM_BUN_DROP_AREA = (By.XPATH, "//span[contains(normalize-space(.), 'Перетяните булочку сюда (низ)')]/ancestor::li")

    INGREDIENT_DROP_AREA = (By.XPATH, "//ul[contains(@class, 'BurgerConstructor_basket__list')]")

    CREATE_ORDER_BUTTON = (By.XPATH, "//button[contains(normalize-space(.), 'Оформить заказ')]")

    ORDER_NUMBER_IN_MODAL = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    ORDER_MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")


class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[contains(normalize-space(.), 'Email')]/parent::div/input")
    PASSWORD_INPUT = (By.XPATH, "//label[contains(normalize-space(.), 'Пароль')]/parent::div/input")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(normalize-space(.), 'Войти')]")
    REGISTER_LINK = (By.XPATH, "//a[contains(normalize-space(.), 'Зарегистрироваться')]")


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//label[contains(normalize-space(.), 'Имя')]/parent::div/input")
    EMAIL_INPUT = (By.XPATH, "//label[contains(normalize-space(.), 'Email')]/parent::div/input")
    PASSWORD_INPUT = (By.XPATH, "//label[contains(normalize-space(.), 'Пароль')]/parent::div/input")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(normalize-space(.), 'Зарегистрироваться')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(normalize-space(.), 'Войти')]")


class FeedPageLocators:
    ORDER_FEED_TITLE = (By.XPATH, "//h1[contains(normalize-space(.), 'Лента заказов')]")

    TOTAL_COUNTER = (
        By.XPATH,
        "//p[contains(normalize-space(.), 'Выполнено за все время') or contains(normalize-space(.), 'Выполнено за всё время')]/following-sibling::p"
    )

    TODAY_COUNTER = (
        By.XPATH,
        "//p[contains(normalize-space(.), 'Выполнено за сегодня')]/following-sibling::p"
    )

    ORDERS_IN_PROGRESS = (By.XPATH, "//*[contains(normalize-space(.), 'В работе')]/following-sibling::*")