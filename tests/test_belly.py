import pytest
from src.tiempo_parser import parse_tiempo

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