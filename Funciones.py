def salir(arreglo):
    print("Sebastian Hurtado 06/07/2023")


def llenar(arreglo):
    x = 1
    for f in range(10):
        for c in range(10):
            if len(str(x)) == 1:
                arreglo[f][c] = '0' + str(x)
            else:
                arreglo[f][c] = str(x)
            x = x + 1


def mostrar(arreglo):
    for f in range(10):
        fila = ''
        for c in range(10):
            fila = fila + ' | ' + arreglo[f][c]
        print(fila)


def marcarAsiento(arreglo, num_entrada):
    x = 1
    for f in range(10):
        for c in range(10):
            if x == num_entrada:
                arreglo[f][c] = 'XX'
            x = x + 1


def verificarEntrada(arreglo, num_entrada):
    x = 1
    for f in range(10):
        for c in range(10):
            if x == num_entrada:
                arreglo[f][c] = 'XX'
                return True
            x = x + 1
    return False


def validarRut():
    while True:
        try:
            rut = int(input("Ingrese Rut:"))
            if len(str(rut)) == 8:
                return rut
            else:
                print("Error: Rut debe ser de 8 digitos, sin numero verificador (12345678)")
        except BaseException as error:
            print(f"Error: {error}")