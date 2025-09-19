# La asistente académica tiene que verificar el promedio de notas de un estudiante. La lista de estudiantes a verificar son 4,
#  estos estudiantes son: Juan, Marta, Andrea, Ana (Precargados en una función.). 

# La asistente debe ingresar en el programa, (que nosotros vamos a crear) las notas de cada estudiante, 
# cada estudiante tiene 3 notas y el programa debe calcular el promedio para mostrar los resultados en pantalla. 

# Entonces, como programadores debemos: 
# Crear una función para ingresar las notas de cada estudiante.
# Crear una función que reciba la lista de notas y pueda calcular el promedio de notas de cada estudiante y almacenarlo en una lista de promedio
# (El índice de la lista estudiante, corresponde al índice de la lista promedios)
# Imprimir la lista de Estudiantes, sus notas y su promedio de notas. Se debe visualizar la lista de notas con respecto a los estudiantes.

def cargar_estudiantes (lista_nombres: list) -> list:
    lista_estudiantes = [0] 
    for i in range (len(lista_nombres)):
        lista_estudiantes = lista_nombres
    return lista_estudiantes

lista_estudiantes = cargar_estudiantes(["Juan", "Marta", "Andrea", "Ana"])


def ingresar_notas (lista_estudiantes: list) ->list:
    lista_notas = [0] * len(lista_estudiantes)
    for i in range(len(lista_estudiantes)):
        notas_personales = [0] * 3
        for e in range(len(notas_personales)):
            nota = int(input(f"Ingrese la nota del alumno {lista_estudiantes[i]}:  "))
            notas_personales[e] = nota

        lista_notas[i] = notas_personales

    return lista_notas
   
lista_notas = ingresar_notas(lista_estudiantes)


# Crear una función que reciba la lista de notas y pueda calcular el promedio de notas de cada estudiante y almacenarlo en una lista de promedio
def calcular_promedio (lista_notas: list)-> list:
    lista_promedio = [0] * len(lista_notas)

    for i in range(len(lista_notas)):
        suma = 0
        for e in range(3):
            suma += lista_notas[i][e]
            promedio = suma / 3
            lista_promedio[i] = float(promedio)
    
    return lista_promedio

lista_promedio_def = calcular_promedio(lista_notas)

def imprimir_resultados(lista_estudiantes: list, lista_notas: list, lista_promedios: list) -> None:
    for i in range(len(lista_estudiantes)):
        print(f"el estudiante: {lista_estudiantes[i]}consiguió un promedio de: {lista_promedios[i]}debido a sus notas: {lista_notas[i]}")



