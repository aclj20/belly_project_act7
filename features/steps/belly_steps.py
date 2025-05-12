from behave import given, when, then
from src.tiempo_parser import parse_tiempo
from src.pepinos_parser import procesar_pepinos
from src.belly import *

#Modificación: Acepta de entrada un string para cukes
@given('que he comido {cukes} pepinos')
def step_given_eaten_cukes(context, cukes):
    context.excepcion = None
    try:
        cantidad = procesar_pepinos(cukes)
        context.belly.comer(cantidad)
    except Exception as e:
        context.excepcion = e

@when('espero {time_description}')
def step_when_wait_time_description(context, time_description):
    total_time_in_hours = parse_tiempo(time_description)
    print("DEBUG - Horas interpretadas:", total_time_in_hours)
    context.belly.esperar(total_time_in_hours)

@when('consulto cuántos pepinos he ingerido')
def step_when_consultar_pepinos(context):
    context.resultado = context.belly.pepinos_ingestados()

@when('pregunto cuántos pepinos más puedo comer')
def step_when_pregunto_pepinos_restantes(context):
    context.pepinos_restantes = max(0, 10 - context.belly.pepinos_comidos)

@then('debería decirme que puedo comer {esperado} pepinos más')
def step_then_decir_pepinos_mas(context, esperado):
    assert context.pepinos_restantes == int(esperado), f"Esperado {esperado}, pero fue {context.pepinos_restantes}"

@then('debería decirme que no puedo comer más pepinos')
def step_then_no_puede_comer_mas(context):
    assert context.pepinos_restantes == 0, f"Se esperaba que no se pueda comer más, pero quedan {context.pepinos_restantes}"
    
@then('debería ver que he comido {esperado} pepinos')
def step_then_verificar_total(context, esperado):
    cantidad = procesar_pepinos(esperado)
    assert context.resultado == cantidad

@then('mi estómago debería gruñir')
def step_then_belly_should_growl(context):
    assert context.belly.esta_gruñendo(), "Se esperaba que el estómago gruñera, pero no lo hizo."

@then('mi estómago no debería gruñir')
def step_then_belly_should_not_growl(context):
    assert not context.belly.esta_gruñendo(), "Se esperaba que el estómago no gruñera, pero lo hizo."

@then('mi estómago puede gruñir')
def step_then_belly_should_not_growl(context):
    pass

@then('debería ocurrir un error de cantidad negativa.')
def step_then_error_negativa(context):
    assert context.excepcion is not None, "Se esperaba una excepción, pero no se lanzó ninguna."
    assert isinstance(context.excepcion, ValueError), "Se esperaba una ValueError."
    assert str(context.excepcion) == "No se puede comer una cantidad negativa de pepinos"

@then('debería ocurrir un error de cantidad invalida.')
def step_then_error_invalida(context):
    assert context.excepcion is not None, "Se esperaba una excepción, pero no se lanzó ninguna."
    assert isinstance(context.excepcion, ValueError), "Se esperaba una ValueError."
    assert str(context.excepcion) == "No se pueden comer más de 100 pepinos"
