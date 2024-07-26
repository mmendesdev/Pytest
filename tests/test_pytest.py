from codigo.jogo import brincadeira

"""
 O teste é formado por 3 etapas (GWT - AAA)
-Given - Dado
-When - Quando
-Then - Então

-ARANGE
-ACT
-ASSERT
"""


def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    entrada = 1  # dado
    esperado = 1  # dado

    resultado = brincadeira(4)  # When
    assert resultado == esperado  # Then

    entrada.close()


def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
    assert brincadeira(2) == 2


def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
    assert brincadeira(3) == "queijo"
