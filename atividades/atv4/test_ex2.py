from ex2 import * 
import pytest

def test_acordar_cedo():
#Teste se o tipo retornado na função acordar_cedo é str
    assert acordar_cedo(5) != 5
#Teste para conclusão de acordar_cedo
    assert acordar_cedo(5) == 'Você é um guerreiro' 
#Teste para falha de acordar_cedo
    assert acordar_cedo(10) == 'Tente novamente amanhã'

def test_tempo_exercicio():
#Teste para conclusão de tempo_exercicio
    assert tempo_exercicio(60,3) == 59
#Teste para falha de tempo_exercicio
    assert tempo_exercicio(60,1) is None

def test_tem_exercicio():
#Teste para verificar se passar 'Descanso' em tem_exercicio
    assert tem_exercicio('Descanso') == False
# Teste para verificar se passar um esporte como parametro em tem_exercicio
    assert tem_exercicio('Natação') == True



