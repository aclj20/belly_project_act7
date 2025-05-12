import re
import random

random.seed(20)
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
            "ochenta":80, "noventa":90, "media": 0.5,

            "zero": 0, "one": 1, "a": 1, "an": 1, "two": 2, "three": 3, "four": 4, "five": 5,
            "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11,
            "twelve": 12, "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
            "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
            "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
            "eighty": 80, "ninety": 90, "half": 0.5
        }
        return numeros.get(palabra.lower(), 0)


def parse_tiempo(time_description: str) -> float:
    time_description = time_description.strip('"').lower()
    time_description = time_description.replace('y', ' ')
    #Modificación: Reemplaza una coma por un espacio en blanco
    time_description = time_description.replace(',', ' ')
    #Modificación: Reemplaza 'and' por un espacio en blanco
    time_description = time_description.replace('and', ' ')
    time_description = time_description.strip()

    # Modificación: Maneja casos especiales
    if time_description in ('media hora', 'half hour'):
        total_time_in_hours = 0.5
        return total_time_in_hours
    else:
        # Modificación: Expresión regular para extraer limites de tiempo en horas
        pattern0 = re.compile(r'entre\s*(\w+)\s+(\w+)\s*horas?', re.IGNORECASE)
        
        match0 = pattern0.match(time_description)

        # Modificación: Expresión regular para extraer horas o hours, minutos o minutes y segundos o seconds
        pattern = re.compile(
            r'(?:(\w+)\s*(?:horas?|hours?))?\s*'
            r'(?:(\w+)\s*(?:minutos?|minutes?))?\s*'
            r'(?:(\w+)\s*(?:segundos?|seconds?))?',
            re.IGNORECASE
        )

        match = pattern.match(time_description)

        if match0:
            rango_inferior_word = match0.group(1) or "0"
            rango_superior_word = match0.group(2) or "0"

            rango_inferior = convertir_palabra_a_numero(rango_inferior_word)
            rango_superior = convertir_palabra_a_numero(rango_superior_word)

            total_time_in_hours = random.uniform(rango_inferior, rango_superior)

            print(f"Tiempo aleatorio: {total_time_in_hours} horas")
            return total_time_in_hours
        

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



    