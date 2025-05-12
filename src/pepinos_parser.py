def procesar_pepinos(cukes):
    try:
        cukes = float(cukes)
    except ValueError:
        raise ValueError(f"No se pudo convertir '{cukes}' a número")
    
    if cukes < 0:
        raise ValueError("No se puede comer una cantidad negativa de pepinos")
    #if cukes > 100:
       # raise ValueError("No se pueden comer más de 100 pepinos")
    return cukes
