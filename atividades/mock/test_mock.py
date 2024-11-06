import pytest
import requests
from unittest.mock import MagicMock

@pytest.fixture
def mock_response():
    # simulando uma chamada de API
    mock = MagicMock (spec=requests.Response)
    mock.status_code = 200
    mock.json.return_value = {"message": "sucess"}
    return mock

def test_api_chamada_com_mock(mock_response):
    # definindo um retorno para o mock
    response = mock_response
    assert response.status_code == 200
    assert response.json() == {"message": "sucess"}