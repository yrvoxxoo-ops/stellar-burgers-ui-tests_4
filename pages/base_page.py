import allure
from selenium.common.exceptions import ElementClickInterceptedException 
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем страницу")
    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def find_visible_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def find_clickable_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.step("Кликаем по элементу")
    def click_element(self, locator):
        element = self.find_clickable_element(locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Вводим текст в поле")
    def set_text(self, locator, text):
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        return self.find_visible_element(locator).text

    def get_current_url(self):
        return self.driver.current_url

    def is_element_visible(self, locator):
        return self.find_visible_element(locator).is_displayed()

    @allure.step("Перетаскиваем элемент")
    def drag_and_drop(self, source_locator, target_locator):
        source = self.find_visible_element(source_locator)
        target = self.find_visible_element(target_locator)

        browser_name = self.driver.capabilities["browserName"]

        if browser_name == "firefox":
            self.driver.execute_script(
                """
                const source = arguments[0];
                const target = arguments[1];

                const dataTransfer = new DataTransfer();

                const dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });

                const dragOverEvent = new DragEvent('dragover', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });

                const dropEvent = new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });

                source.dispatchEvent(dragStartEvent);
                target.dispatchEvent(dragOverEvent);
                target.dispatchEvent(dropEvent);
                """,
                source,
                target
            )
        else:
            ActionChains(self.driver).drag_and_drop(source, target).perform()
        
    def wait_until_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    def wait_until_text_is_present(self, locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
        
    def wait_until_element_is_not_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))