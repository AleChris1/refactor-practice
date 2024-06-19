import csv
# el programa deberá calcular el ganador de votos validos considerando que los siguientes datos son proporcionados:
# region,provincia,distrito,dni,candidato,esvalido
# Si hay un candidato con >50% de votos válidos retornar un array con un string con el nombre del ganador
# Si no hay un candidato que cumpla la condicion anterior, retornar un array con los dos candidatos que pasan a segunda vuelta
# Si ambos empatan con 50% de los votos se retorna el que apareció primero en el archivo
# el DNI debe ser valido (8 digitos)

class CalculaGanador:
    def leer_datos(self, archivo):
        datos = []
        with open(archivo, 'r') as csvfile:
            next(csvfile)  # Omitir encabezado
            reader = csv.reader(csvfile)
            for fila in reader:
                if self.es_dni_valido(fila[3]):
                    datos.append(fila)
        return datos

    def es_dni_valido(self, dni):
        return len(dni) == 8 and dni.isdigit()

    def contar_votos_validos(self, datos):
        votos_por_candidato = {}
        total_votos_validos = 0

        for fila in datos:
            candidato = fila[4]
            es_valido = fila[5] == '1'
            
            if es_valido:
                if candidato not in votos_por_candidato:
                    votos_por_candidato[candidato] = 0
                votos_por_candidato[candidato] += 1
                total_votos_validos += 1

        return votos_por_candidato, total_votos_validos

    def calcular_ganador(self, datos):
        votos_por_candidato, total_votos_validos = self.contar_votos_validos(datos)
        candidatos_ordenados = sorted(votos_por_candidato.items(), key=lambda item: item[1], reverse=True)
        
        if not candidatos_ordenados:
            return []

        ganador, votos_ganador = candidatos_ordenados[0]
        if votos_ganador > total_votos_validos / 2:
            return [ganador]

        if len(candidatos_ordenados) > 1:
            segundo_candidato = candidatos_ordenados[1][0]
            return [ganador, segundo_candidato]

        return [ganador]

# Ejemplo de uso:
calculador = CalculaGanador()
datos = calculador.leer_datos('0204.csv')
#print(calculador.calcular_ganador(datos))

# Datos de prueba proporcionados en la pregunta:
datos_prueba = [
    ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
    ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
    ['Áncash', 'Asunción', 'Acochaca', '6777322', 'Aundrea Grace', '1'],
    ['Áncash', 'Asunción', 'Acochaca', '3017965', 'Aundrea Grace', '1'],
]
print(calculador.calcular_ganador(datos_prueba))
