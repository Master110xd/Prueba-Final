from Persona import *
from Funciones import *
import numpy as np
arreglo = np.full((10, 10), '--')
lista_Asistentes = []
ciclo = True
llenar(arreglo)


def ingresarAsistente(lista_Asistentes, num_entrada):
    asis = Asistente()
    asis.rut = validarRut()
    asis.num_entrada = num_entrada
    if 1 <= num_entrada <= 20:
        asis.valor = 120000
    if 21 <= num_entrada <= 50:
        asis.valor = 80000
    if 51 <= num_entrada <= 100:
        asis.valor = 50000
    lista_Asistentes.append(asis)


def listarAsistentes(lista_Asistentes):
    for asis in lista_Asistentes:
        print(f"Rut: {asis.rut} Numero de Entrada: {asis.num_entrada} Valor: ${asis.valor}")


def comprarEntrada(arreglo, lista_Asistentes):
    compra = 0
    try:
        cantidad = int(input("Ingrese cuantas entradas desea:"))
        if 1 <= cantidad <= 3:
            while compra < cantidad:
                mostrar(arreglo)
                try:
                    num_entrada = int(input("Ingrese que numero de entrada desea:"))
                    if 1 <= num_entrada <= 100:
                        resp = verificarEntrada(arreglo, num_entrada)
                        if resp:
                            marcarAsiento(arreglo, num_entrada)
                            ingresarAsistente(lista_Asistentes, num_entrada)
                            compra = compra + 1
                    else:
                        print("Error: Lugar ingresado no disponible")
                except BaseException as error:
                    print(f"Error: {error}")
        else:
            print("Error: Solo puede comprar maximo 3 entradas a la vez")
    except BaseException as error:
        print(f"Error: {error}")


def gananciasTotales(lista_Asistentes):
    platinum = 0
    gold = 0
    silver = 0
    totaldeVentas = 0
    totaldeClientes = 0
    for asis in lista_Asistentes:
        match int(asis.valor):
            case 120000:
                platinum = platinum + 1
            case 80000:
                gold = gold + 1
            case 50000:
                silver = silver + 1
        totaldeClientes = platinum + gold + silver
        totaldeVentas = (platinum * 120000) + (gold * 80000) + (silver * 50000)
    print("Tipo Entrada      Cantidad     Total")
    print(f"Platinum $120000     {platinum}         ${platinum * 120000}")
    print(f"Gold     $80000      {gold}         ${gold * 80000}")
    print(f"Silver   $50000      {silver}         ${silver * 50000}")
    print(f"TOTAL                {totaldeClientes}         ${totaldeVentas}")


while ciclo:
    print("Creativos.cl Concierto Michael Jam")
    print("1) Comprar entradas")
    print("2) Mostrar ubicaciones disponibles")
    print("3) Ver listado de asistentes")
    print("4) Mostrar ganancias totales")
    print("5) Salir")
    try:
        opc = int(input("Ingrese una opcion:"))
        match opc:
            case 1:
                comprarEntrada(arreglo, lista_Asistentes)
            case 2:
                mostrar(arreglo)
            case 3:
                listarAsistentes(lista_Asistentes)
            case 4:
                gananciasTotales(lista_Asistentes)
            case 5:
                salir(arreglo)
            case _:
                print("Error: Opcion ingresada no valida, debe ser de 1 a 5")
    except BaseException as error:
        print(f"Error: {error}")
