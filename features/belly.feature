# language: es

Característica: Característica del estómago
  @spanish
  Escenario: comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  @spanish
  Escenario: comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir
  
  @spanish
  Escenario: comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir
  
  @spanish
  Escenario: comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: comer pepinos y esperar en segundos
    Dado que he comido 5 pepinos
    Cuando espero 3000 segundos
    Entonces mi estómago no debería gruñir

  @spanish
  Escenario: comer pepinos y esperar en varios formatos
    Dado que he comido 30 pepinos
    Cuando espero "1 hora, 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: Comer una cantidad fraccionaria de pepinos
    Dado que he comido 0.5 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  @spanish
  Escenario: Comer una cantidad negativa de pepinos
    Dado que he comido -3 pepinos
    Cuando espero 2 horas
    Entonces debería ocurrir un error de cantidad negativa.

# @spanish
# Escenario: Comer una cantidad mayor a 100 de pepinos
#   Dado que he comido 200 pepinos
#   Cuando espero 4 horas
#   Entonces debería ocurrir un error de cantidad invalida.

  @spanish 
  Escenario: Comer pepinos y esperar un tiempo aleatorio
    Dado que he comido 40 pepinos
    Cuando espero "entre 1 y 2 horas"
    Entonces mi estómago puede gruñir

  @spanish 
  Escenario: Comer 1000 pepinos y esperar 10 horas
    Dado que he comido 1000 pepinos
    Cuando espero 10 horas
    Entonces mi estómago debería gruñir

  @spanish
  Escenario: Comer muchos pepinos y esperar el tiempo suficiente
    Dado que he comido 15 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  @english
  Escenario: Esperar usando horas en inglés
    Dado que he comido 20 pepinos
    Cuando espero "two hours and thirty minutes"
    Entonces mi estómago debería gruñir
  
  @english
  Escenario: Esperar usando "half" en inglés
    Dado que he comido 20 pepinos
    Cuando espero "half hour"
    Entonces mi estómago no debería gruñir 

  @spanish
  Escenario: Comer suficientes pepinos y esperar el tiempo adecuado
  Dado que he comido 20 pepinos
  Cuando espero 2 horas
  Entonces mi estómago debería gruñir
  
  @spanish
  Escenario: Comer pocos pepinos y no esperar suficiente tiempo
    Dado que he comido 5 pepinos
    Cuando espero 1 hora
    Entonces mi estómago no debería gruñir
  
  @spanish
  Escenario: Comer una cantidad específica de pepinos
    Dado que he comido 15 pepinos
    Cuando consulto cuántos pepinos he ingerido
    Entonces debería ver que he comido 15 pepinos

  @spanish
  Escenario: Predecir si mi estómago gruñirá tras comer y esperar
    Dado que he comido 12 pepinos
    Cuando espero 1 hora y 30 minutos
    Entonces mi estómago debería gruñir
  
  @criterio_nuevo
  Escenario: Comer menos de 10 pepinos y preguntar cuantos pepinos puedo comer antes de que el estómago gruña
    Dado que he comido 8 pepinos
    Cuando pregunto cuántos pepinos más puedo comer
    Entonces debería decirme que puedo comer 2 pepinos más

  @criterio_nuevo
  Escenario: Comer más de 10 pepinos y preguntar cuantos pepinos puedo comer antes de que el estómago gruña
    Dado que he comido 12 pepinos
    Cuando pregunto cuántos pepinos más puedo comer
    Entonces debería decirme que no puedo comer más pepinos
