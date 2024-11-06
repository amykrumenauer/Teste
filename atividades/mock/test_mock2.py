import requests

# função que faz uma chamada a uma API
def obter_dados_da_api(url):
    resposta = requests.get(url)
    return resposta.json()

# teste sem fazer a chamada real à API
def test_obter_dados_da_api(mocker):
    
    # mockando a resposta da função requests.get
    mock_response = mocker.patch ('requests.get')
    
    # definindo um retorno fictício para o mock
    mock_response.return_value.json.return_value = {"id": 1, "nome": "Teste"}
    
    # testando a função com o mock
    resultado = obter_dados_da_api("http://api.exemplo.com/dados")
    
    # verificando se o resultado é esperado
    assert resultado == {"id": 1, "nome": "Teste"}