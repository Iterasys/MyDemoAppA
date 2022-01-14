from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class BasePage:
    def __init__(self, driver):
        self.driver = driver  # Este é o nosso Appium (primo do Selenium)

    def _iniciar(self, url, caps):
        # self.driver.get(url)                      # abrir uma página no Selenium
        self.driver = webdriver.Remote(url, caps)  # iniciar o app no Appium

    def _localizar(self, locator):
        return self.driver.find_element(locator['by'], locator['value'])

    def _apertar(self, locator):
        self._localizar(locator).click()

    def _escrever(self, locator, texto):
        self._localizar(locator).send_keys(texto)

    def _ler(self, locator):
        self._localizar(locator).text()

    def _rolar(self, origem_x, origem_y, destino_x, destino_y):
        TouchAction(self.driver).press(x=origem_x, y=origem_y).move_to(x=destino_x, y=destino_y).release().perform()
