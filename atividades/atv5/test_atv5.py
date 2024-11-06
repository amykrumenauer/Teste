import pytest
from unittest.mock import MagicMock
import requests
from test_banco import BancoDeDados, calcular_valor_total, obter_pedido_com_valor_total

# 1. Teste para calcular_valor_total()
@pytest.fixture
def mock_api_response():
    # Dados fictícios de resposta da API
    return [
        {"preco": 100.0, "quantidade": 2},
        {"preco": 50.0, "quantidade": 1}
    ]

def test_calcular_valor_total(mock_api_response, mocker):
    # Usamos o mock para a chamada à API externa
    mocker.patch("requests.get", return_value=MagicMock(json=lambda: mock_api_response))

    # Verifica se o cálculo está correto
    pedido_id = 1
    resultado = calcular_valor_total(pedido_id)
    assert resultado == 250.0, f"Esperado 250.0, mas obteve {resultado}"

# 2. Fixture para simular o banco de dados
@pytest.fixture
def mock_banco():
    banco = MagicMock(BancoDeDados)
    banco.buscar_pedido.return_value = {"id": 1, "cliente": "João"}
    return banco

# 3. Teste para obter_pedido_com_valor_total()
def test_obter_pedido_com_valor_total(mock_banco, mock_api_response, mocker):
    # Usamos o mock para a chamada à API externa
    mocker.patch("requests.get", return_value=MagicMock(json=lambda: mock_api_response))

    # Simula a obtenção do pedido com o valor total calculado
    pedido_id = 1
    pedido_com_valor = obter_pedido_com_valor_total(pedido_id, mock_banco)
    
    # Verifica se o valor total foi adicionado corretamente ao pedido
    assert pedido_com_valor["valor_total"] == 250.0, f"Esperado valor total 250.0, mas obteve {pedido_com_valor['valor_total']}"
    assert pedido_com_valor["cliente"] == "João", f"Esperado cliente João, mas obteve {pedido_com_valor['cliente']}"
