import pytest
from src.tiempo_parser import parse_tiempo
from src.pepinos_parser import procesar_pepinos
from unittest.mock import MagicMock
from src.belly import *

@pytest.mark.parametrize("input_str, expected", [
    ("una hora", 1.0),
    ("dos horas", 2.0),
    ("media hora", 0.5),
    ("una hora y quince minutos", 1.25),
    ("quince minutos", 0.25),
    ("tres minutos", 0.05),
    ("una hora cinco minutos", 1 + 5/60),
    ("una hora, cinco minutos", 1 + 5/60),
    ("dos horas veinte minutos cinco segundos", 2 + 20/60 + 5/3600),
    ("cinco segundos", 5/3600),
])
def test_parse_tiempo(input_str, expected):
    resultado = parse_tiempo(input_str)
    assert abs(resultado - expected) < 0.0001

@pytest.mark.parametrize("input_str", [
    "-1",
    "-0.5",
    "-10.4",
])

def test_procesar_pepinos_negativo(input_str):
    with pytest.raises(ValueError, match="No se puede comer una cantidad negativa de pepinos"):
        procesar_pepinos(input_str)

@pytest.mark.parametrize("input_str, expected", [
    ("3", 3.0),
    ("2.5", 2.5),
    ("0", 0.0),
    ("0.6", 0.6),
    ("1.5", 1.5),
])
def test_parse_pepinos_valido(input_str, expected):
    resultado = procesar_pepinos(input_str)
    assert abs(resultado - expected) < 0.0001

def test_gruñir_si_comido_muchos_pepinos():
    belly = Belly()
    belly.comer(15)
    belly.esperar(2)
    assert belly.esta_gruñendo() == True

def test_pepinos_restantes():
    belly = Belly()
    belly.comer(15)
    assert belly.pepinos_ingestados() == 15

@pytest.mark.parametrize(
    "pepinos, horas, esperado",
    [
        (20, 2, True),      
        (8, 2, False),     
        (15, 1.0, False),   
        (12, 1.6, True),    
    ]
)
def test_estomago_gruñendo_parametrizado(pepinos, horas, esperado):
    belly = Belly()
    belly.comer(pepinos)
    belly.esperar(horas)
    assert belly.esta_gruñendo() == esperado

def test_estomago_predecir_gruñido():
    belly = Belly()
    belly.comer(12)
    belly.esperar(1.5)
    assert belly.esta_gruñendo() == True

def test_tiempo_controlado():
    reloj_falso = MagicMock(return_value=12345)  
    belly = Belly(clock_service=reloj_falso)
    assert belly.clock_service() == 12345