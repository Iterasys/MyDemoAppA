from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ProdutoPage(BasePage):
    # localizadores
    _nome_produto = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/productTV'}
    _preco_produto = {'by': AppiumBy.ID, 'value': 'com.saucelabs.mydemoapp.android:id/priceTV'}
    _origem_x = 956
    _origem_y = 2058
    _destino_x = 898
    _destino_y = 451
    _color_image_view = {'by': AppiumBy.XPATH, 'value': '(//android.widget.ImageView[@content-desc=\"Displays color of product\"])[3]'}
    _aumentar_quantidade = {'by': AppiumBy.ACCESSIBILITY_ID, 'value': 'Increases number of products'}
    _adicionar_carrinho = {'by': AppiumBy.ACCESSIBILITY_ID, 'value': 'Tap to add product to cart'}


    # inicializar
    def __init__(self, driver):
        self.driver = driver
        # poderia validar se abriu a tela correta

    # ações
    # validar o produto e o preço
    def validar_nome(self):
        return self._localizar(self._nome_produto).text

    def validar_preco(self):
        return self._localizar(self._preco_produto).text

    # continuar o fluxo de compra
    def arrastar_para_cima(self):
        self._rolar(
            self._origem_x,
            self._origem_y,
            self._destino_x,
            self._destino_y
        )

    def como_(self, quantidade):
        # selecionar a cor da mochila como cinza(?)
        self._apertar(self._color_image_view)

        # selecionar a quantidade do produto
        # como já vem selecionado 1 produto, se for apenas 1 para comprar, não é necessário
        # clicar no elemento. Se forem 2 produtos, clica 1 vez, se forem 3, clica 2 vezes
        for itens in range(quantidade - 1):
            self._apertar(self._aumentar_quantidade)

        # adicionar o produto no carrinho
        self._apertar(self._adicionar_carrinho )

    # ir para o carrinho de compras