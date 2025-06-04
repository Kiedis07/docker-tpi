#BATISTA BOVIO TPI AYSO
# python_app/app.py

def calcular_promedio(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

if __name__ == "__main__":
    print("¡Calculadora de Promedios!")
    print("Ingresa números separados por comas para calcular su promedio.")
    print("Para salir, escribe 'fin' o 'salir'.") 

    while True:
        entrada = input("Números: ")

        # Agregamos esta parte 
        if entrada.lower() in ('fin', 'salir'): # Convertimos a minúsculas para aceptar 'FIN', 'Salir', etc.
            print("¡Gracias por usar la calculadora! Saliendo...")
            break # Rompe el bucle while y termina el programa
        
        try:
            lista_numeros = [float(n.strip()) for n in entrada.split(',')]
            promedio = calcular_promedio(lista_numeros)
            print(f"El promedio es: {promedio:.2f}")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa solo números separados por comas.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")