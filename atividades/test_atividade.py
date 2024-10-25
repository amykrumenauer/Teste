# Função de verificação de email
def email_valido(email): 
    return '@' in email and '.' in email 

def test_email():
    email = 'krumenaueramy5@gmail.com'
    assert email_valido(email) == True

# Função para verificar se um número é par  
def eh_par(n): 
	return n % 2 == 0

def test_par():
    n = 8
    assert eh_par(n) == True

# Função para calcular o fatorial 
def fatorial(n): 
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def test_fatorial():
    n = 4
    assert fatorial(n) == 24

# Função verificar quadrado
def quadrado(n): 
	return n ** 2

def test_quadrado():
    n = 2 
    assert quadrado(n) == 4

# Função de é positivo
def eh_positivo(n):
	return n > 0

def test_positivo():
    n = 1
    assert eh_positivo(n) == True
    
# Função verificar maior idade
def verificar_maioridade(idade):
    if idade >= 18:
        return 'maior de idade'
    else:
        return 'menor de idade'

def test_maioroumenor():
    assert verificar_maioridade(18) == 'maior de idade'


# Função classificar temperatura
def classificar_temperatura(temp):
    if temp < 0:
        return 'frio'
    elif 0 <= temp <= 25:
        return 'moderado'
    else:
        return 'quente'
    
def test_temperatura():
    assert classificar_temperatura(-5) == 'frio'
    assert classificar_temperatura(0) == 'moderado'
    assert classificar_temperatura(20) == 'moderado'
    assert classificar_temperatura(30) == 'quente'
    
def avaliar_nota(nota):
    if nota >= 7:
        return 'aprovado'
    elif 5 <= nota < 7:
        return 'recuperacao'
    else:
        return 'reprovado'

def test_nota():
    assert avaliar_nota(10) == 'aprovado'

def pode_votar(idade):
    if idade >= 18:
        return 'voto obrigatório'
    elif 16 <= idade < 18:
        return 'voto facultativo'
    else:
        return 'não pode votar'

def test_voto():
    assert pode_votar(10) == 'não pode votar'

def avaliar_produto(estrelas):
    if estrelas == 5:
        return 'excelente'
    elif estrelas == 4:
        return 'bom'
    elif estrelas == 3:
        return 'regular'
    elif estrelas == 2:
        return 'ruim'
    elif estrelas == 1:
        return 'péssimo'
    else:
        return 'valor inválido'

def test_produto():
    assert avaliar_produto(4) == 'bom'
