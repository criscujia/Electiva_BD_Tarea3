
from os import system

def agregar(vec,diccionario):
    system("cls")
    diccionario = {}

    diccionario ['id'] = input("Ingresa el id del funcionario >> ")
    diccionario ['Nombre'] = input("Ingresa el nombre del funcionario >> ")
    diccionario ['Cargo'] = input("Ingresa el cargo del funcionario >> ")
    diccionario ['Salario'] = input("Ingresa el salario del funcionario >> ")
    
    vec.append(diccionario)


def mostrar(vec,diccionario):
    system("cls")

    print ("-----------------------------------------------------------------------")
    for dic in vec:
        for llave in dic:
            print(f'{llave} : {dic[llave]}')
        print ("-----------------------------------------------------------------------")
    if not vec:
        print(f'No existen funcionarios')


def buscar(vec,diccionario):
    system("cls")
    bus = input("Ingresa el nombre del funcionario a buscar >> ")
    b = 0

    for busdic in vec:
        if busdic["Nombre"] == bus:
            b = 1
            print(f'Los datos del funcionario {bus} son: ')
            for llave in busdic:
                print(f'{llave} : {busdic[llave]}')
            print ("-----------------------------------------------------------------------")
    if b == 0:
        print(f'\nFuncionario {bus} no encontrado\n')
    print ("-----------------------------------------------------------------------")    



def eliminar(vec,diccionario):
    system("cls")
    el = input("Ingresa el nombre del funcionario a eliminar >> ")
    b = 0

    for eldic in vec:
        if eldic["Nombre"] == el:
            b = 1
            vec.remove(eldic)
            print(f'Los datos del funcionario {el} han sido eliminados ')
    if b == 0:
        print(f'\nFuncionario {el} no encontrado\n')
    print ("-----------------------------------------------------------------------")    
    
