import pytest
from pages import inicial_page, produto_page, carrinho_page


# inicializações das classes de páginas
@pytest.fixture()
def inicial(driver):  # inicializar a inicial_page
    return inicial_page.InicialPage(driver)


@pytest.fixture()
def produto(driver):  # inicializar a produto_page
    return produto_page.ProdutoPage(driver)


@pytest.fixture()
def carrinho(driver):  # inicializar a carrinho_page
    return carrinho_page.CarrinhoPage(driver)


# os testes

# teste positivo do fluxo de compras
def testar_comprar_mochila_cinza(inicial, produto, carrinho,
                                 quantidade=2,
                                 nome_produto_esperado='Sauce Lab Back Packs',
                                 preco_produto_esperado='$ 29.99',
                                 total_produto_esperado='$ 59.98'
                                 ):
    inicial.selecionar_primeiro_produto_()

    assert produto.validar_nome() == nome_produto_esperado
    assert produto.validar_preco() == preco_produto_esperado
    produto.arrastar_para_cima()
    produto.como_(quantidade)  # 2 mochilas cinzas

    carrinho.ir_para_o_carrinho_de_compras()
    # resultado = carrinho.ler_dados_do_carrinho()

    '''
    assert resultado._titulo_produto == nome_produto_esperado
    assert resultado._preco_produto == preco_produto_esperado
    assert resultado._preco_total == total_produto_esperado
    '''

    assert carrinho.ler_dados_do_carrinho() == [nome_produto_esperado, preco_produto_esperado,
                                                total_produto_esperado]

