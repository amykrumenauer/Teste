# INSTALAR PYTHON ANTES !!!
- Para verificar a versão e se está instalado no computador:
python --version
- Para confirmar se o pip está disponível:
python -m pip --version
- Para instalar:
pip install pytest
- Para criar um novo ambiente virtual:
python -m venv nome_do_ambiente
- Para ativar:
.\nomedoambiente\Scripts\activate
- Para rodar:
pytest
- Para voltar uma pasta: 
cd ..

- Para criar a tabela de rendimento:
- python -m pip install pytest-cov
- python -m pytest --cov
- pytest -v para mostrar PASSED

Fixture:
- Prepara o ambiente para os testes, economizando recursos e criando ambientes isolados.
Mock:
- Simula partes do código, como chamadas de API externas, durante os testes.
- pip install requests
- pip install pytest-mock

