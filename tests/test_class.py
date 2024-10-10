from codigo.test_exemplo import mult, somar


def test_somar():
    assert somar(10, 20) == 30


def test_mult():
    assert mult(10, 10) == 100
