from random import choice, randrange
from datetime import datetime

# Operadores posibles
operators = ["+", "-", "*", "/"]
# Cantidad de cuentas a resolver
times = 5
# Contador inicial de tiempo.
# Esto toma la fecha y hora actual.
init_time = datetime.now()
print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")

count_correct = 0
count_incorrect = 0
for i in range(0, times):
    # Se eligen números y operador al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
   

    #Se asegura que la división no sea por 0
    while operator == "/" and number_2 == 0:
        number_2 = randrange(10)


    # Se imprime la cuenta.
    print(f"{i+1}- ¿Cuánto es {number_1} {operator} {number_2}?")
    # Le pedimos al usuario el resultado
    result = float(input("resultado: "))

    #Se calcula el resultado correcto
    match operator:
        case "+":
            correct_result = number_1 + number_2
        case "-":
            correct_result = number_1 - number_2
        case "*":
            correct_result = number_1 * number_2
        case "/":
            correct_result = number_1 / number_2
    
    #Se imprime si el resultado fue correcto o incorrecto
    if (correct_result != result):
        print("Resultado incorrecto")
        count_incorrect+= 1
    else:
        print("Resultado correcto")
        count_correct+= 1



# Al terminar toda la cantidad de cuentas por resolver.
# Se vuelve a tomar la fecha y la hora.
end_time = datetime.now()
# Restando las fechas obtenemos el tiempo transcurrido.
total_time = end_time - init_time
# Mostramos ese tiempo en segundos.
print(f"\n Tardaste {total_time.seconds} segundos.")

print(f"Tuviste {count_correct} respuestas correctas y {count_incorrect} respuestas incorrectas.")

