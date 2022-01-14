from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class InicialPage(BasePage):
    # localizadores / locators
    image_view_locator = '(//android.widget.ImageView[@content-desc=\"Displays selected product\"])[1]'
    _product_image_view = {'by': AppiumBy.XPATH, 'value': image_view_locator}

    # mapeariamos também os demais elementos da tela

    # inicialização
    def __init__(self, driver):
        self.driver = driver
        # self._iniciar()
        # poderiamos realizar um assert de algum elemento para validar se é a tela certa

    # ações
    def selecionar_primeiro_produto_(self):
        self._apertar(self._product_image_view)
