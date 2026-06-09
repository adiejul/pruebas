def calcular_suma(num1, num2):
    
    """
    ejercicio para practicar pytest, se pide por pantalla dos numeros para obtener su suma
    
    parametros:
        argumentos a sumar
        num1: int
        num2: int
    
    devuelve:
        int: resultado de la suma
        
    """
    
    total = num1 + num2
    
    return total

if __name__ == "__main__":
    
    try: 
        
        num1 = int(input("Introduce el primer numero: "))
        num2 = int(input("Introduce el segundo numero: "))
        
        resultado= calcular_suma(num1, num2)
    
        print(f"el resultado de la suma es {resultado}")
        
    except:
        print("El numero introducido no es correcto")
    
    
