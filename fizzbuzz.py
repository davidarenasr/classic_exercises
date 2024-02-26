#escribie un programa que muetre por consola con un print () los numeros del 1 al 100, ambos por consola y con 
# un salto de linea entre cada expression. sustituyendo los sigueintes: 
#multiplos de 3 por la palabra fizz
#multplicos de 5 por la palabra "buzz"
#multiplos de 3 y de 5 a la vez por la palabra fizzbuzz.

def main():
    bizzbuzz()  # Un ejemplo simple, puedes agregar tu propia lógica aquí

def bizzbuzz():
    for number in range(0, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("bizzbuzz")
        elif number % 3 == 0:
            print("bizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)

# Llamada a la función main
if __name__ == "__main__":
    main()


