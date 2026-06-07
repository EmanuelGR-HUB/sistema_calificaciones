import pytest
from src.calificaciones import calcular_promedio

def test_estudiante_aprobado():
    resultado = calcular_promedio([80, 75, 90])
    assert resultado["estado"] == "Aprobado"
    assert resultado["promedio"] == 81.67

def test_estudiante_reprobado():
    resultado = calcular_promedio([50, 60, 55])
    assert resultado["estado"] == "Reprobado"

def test_exactamente_en_umbral():
    """70 es exactamente el umbral, debe aprobar"""
    resultado = calcular_promedio([70])
    assert resultado["estado"] == "Aprobado"

def test_lista_vacia_lanza_excepcion():
    with pytest.raises(ValueError):
        calcular_promedio([])

def test_nota_maxima():
    resultado = calcular_promedio([100])
    assert resultado["promedio"] == 100.0
    assert resultado["estado"] == "Aprobado"

def test_nota_minima():
    resultado = calcular_promedio([0])
    assert resultado["estado"] == "Reprobado"