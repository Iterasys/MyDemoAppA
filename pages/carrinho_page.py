from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class CarrinhoPage(BasePage):
    # localizadores
    _icone_carrinho = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/cartIV'}
    _titulo_produto = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/titleTV'}
    _preco_produto = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/priceTV'}
    _preco_total = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/totalPriceTV'}

    # inicialização
    def __init__(self, driver):
        self.driver = driver

    # ir para o carrinho de compras
    def ir_para_o_carrinho_de_compras(self):
        self._apertar(self._icone_carrinho)

    # ler os dados do produto no carrinho
    def ler_dados_do_carrinho(self):
        dados = {
            'titulo_produto': self._localizar(self._titulo_produto).text,
            'preco_produto': self._localizar(self._preco_produto).text,
            'preco_total': self._localizar(self._preco_total).text
        }
        return [dados['titulo_produto'], dados['preco_produto'], dados['preco_total']]

