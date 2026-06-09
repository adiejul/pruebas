
from app.operaciones import calcular_suma

def test_operaciones_positivos():
    resultado = calcular_suma(2, 2)
    assert resultado == 4

def test_operaciones_negativos():
    assert calcular_suma(-1, -1) == -2

def test_operaciones_cero():
    assert calcular_suma(5, 0) == 5
    
def test_operaciones_error():
    assert calcular_suma(2, 2) ==5
    
