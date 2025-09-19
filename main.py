from funciones import cargar_estudiantes, ingresar_notas, calcular_promedio, imprimir_resultados

lista_estudiantes = cargar_estudiantes(["Juan", "Marta", "Andrea", "Ana"])
print(lista_estudiantes)
lista_notas = ingresar_notas(lista_estudiantes)
lista_promedios = calcular_promedio(lista_notas)
imprimir_resultados(lista_estudiantes, lista_notas, lista_promedios)