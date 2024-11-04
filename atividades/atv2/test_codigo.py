import math

# Função para Soma
def soma (a,b):
    return a + b
def test_soma ():
    assert soma (5,10) == 15
    assert soma (1, 10) == 11

# Função para Subtração
def subs (a,b):
    return a - b
def test_subs ():
    assert subs (5,10) == -5
    assert subs (1,10) == -9

# Função para Multiplicação
def mult (a,b):
    return a * b
def test_mult ():
    assert mult (5,10) == 50
    assert mult (1,10) == 10

# Função para Divisão
def div (a,b):
    if b == 0:
        return "Para de ser burro"
    else:
        return a / b  
def test_div ():
    assert div (5,10) == 0.5
    assert div (1,10) == 0.1
    assert div (10,0) == "Para de ser burro"

# Função extra para Potenciação
def pot (a,b):
    return a ** b
def test_pot ():
    assert pot (5,2) == 25
    assert pot (1,10) == 1

# Função para calcular a área de um Círculo
def area_circulo(raio):
    if raio < 0:
        return "Erro: o raio não pode ser negativo."
    else:
        return math.pi * (raio ** 2)
    
def test_area_circulo():
    assert area_circulo (5) == 78.53981633974483
    assert area_circulo (-2) == "Erro: o raio não pode ser negativo."

# Função para calcular a área de um Retângulo
def area_retangulo(largura, altura):
    if largura < 0 or altura < 0:
        return "Erro: largura e altura devem ser não-negativos."
    else:
        return largura * altura
    
def test_area_retangulo():
    assert area_retangulo (5,10) == 50
    assert area_retangulo (-2,10) == "Erro: largura e altura devem ser não-negativos."
    assert area_retangulo (1,-8) == "Erro: largura e altura devem ser não-negativos."
    
