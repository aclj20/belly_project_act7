import re

# Función para convertir palabras numéricas a números
def convertir_palabra_a_numero(palabra):
    try:
        return int(palabra)
    except ValueError:
        numeros = {
            "cero": 0, "uno": 1, "una":1, "dos": 2, "tres": 3, "cuatro": 4, "cinco": 5,
            "seis": 6, "siete": 7, "ocho": 8, "nueve": 9, "diez": 10, "once": 11,
            "doce": 12, "trece": 13, "catorce": 14, "quince": 15, "dieciséis": 16,
            "diecisiete":17, "dieciocho":18, "diecinueve":19, "veinte":20,
            "treinta": 30, "cuarenta":40, "cincuenta":50, "sesenta":60, "setenta":70,
            "ochenta":80, "noventa":90, "media": 0.5
        }
        return numeros.get(palabra.lower(), 0)


def parse_tiempo(time_description: str) -> float:
    time_description = time_description.strip('"').lower()
    time_description = time_description.replace('y', ' ')
    #Modificación: Reemplaza una coma por un espacio en blanco
    time_description = time_description.replace(',', ' ')
    time_description = time_description.strip()

    # Manejar casos especiales como 'media hora'
    if time_description == 'media hora':
        total_time_in_hours = 0.5
        return total_time_in_hours
    else:
        # Modificación: Expresión regular para extraer horas, minutos y segundos
        pattern = re.compile(r'(?:(\w+)\s*horas?)?\s*(?:(\w+)\s*minutos?)?\s*(?:(\w+)\s*segundos?)?')
        match = pattern.match(time_description)

        if match:
            #Modificación: Agrega la lógica para segundos
            hours_word = match.group(1) or "0"
            minutes_word = match.group(2) or "0"
            seconds_word = match.group(3) or "0"

            hours = convertir_palabra_a_numero(hours_word)
            minutes = convertir_palabra_a_numero(minutes_word)
            seconds = convertir_palabra_a_numero(seconds_word)
            total_time_in_hours = hours + (minutes / 60) + (seconds / 3600)
            return total_time_in_hours
        else:
            raise ValueError(f"No se pudo interpretar la descripción del tiempo: {time_description}")



    