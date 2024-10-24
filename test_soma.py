def soma (a,b):
    return a + b

def subs (a,b):
    return a - b

def mult (a,b):
    return a * b

def div (a,b):
    if b == 0:
        return "Para de ser burro"
    else:
        return a / b

def pot (a,b):
    return a ** b

def test_soma ():
    assert soma (5,10) == 15
    assert soma (1, 10) == 11

def test_subs ():
    assert subs (5,10) == -5
    assert subs (1,10) == -9

def test_mult ():
    assert mult (5,10) == 50
    assert mult (1,10) == 10

def test_div ():
    assert div (5,10) == 0.5
    assert div (1,10) == 0.1
    assert div (10,0) == "Para de ser burro"

def test_pot ():
    assert pot (5,2) == 25
    assert pot (1,10) == 1
