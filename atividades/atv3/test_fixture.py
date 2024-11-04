import pytest

@pytest.fixture
def lista_simples():
    return [1, 2, 3, 4, 5]

def test_soma(lista_simples):
    assert sum(lista_simples) == 15

def test_tamanho_da_lista(lista_simples):
    assert len(lista_simples) == 5

# Soma em dobro
@pytest.fixture
def lista_dobro():
    return [1, 2, 3, 4, 5]

def soma_dobro(lista):
    return sum(x * 2 for x in lista)

def test_soma_dobro(lista_dobro):
    assert soma_dobro(lista_dobro) == 30
