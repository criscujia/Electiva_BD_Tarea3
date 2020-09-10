from library.ejercicios import*
from os import system

def main():
    while True:        

        print ("Selecciona una opción")
        print ("\t1 - Insertar")
        print ("\t2 - Mostrar")
        print ("\t3 - Buscar")
        print ("\t4 - Eliminar")
        print ("\t5 - Salir")

        opcionMenu = input("inserta un numero valor >> ")

        if opcionMenu=="1":  
            agregar(vec,diccionario)
            input("\npulse una tecla para continuar")
            system("cls")
        elif opcionMenu=="2":
            mostrar(vec,diccionario)
            input("\npulse una tecla para continuar")
            system("cls")
        elif opcionMenu=="3":
            buscar (vec,diccionario)
            input("\npulse una tecla para continuar")
            system("cls")
        elif opcionMenu=="4":
            eliminar (vec,diccionario)
            input("\npulse una tecla para continuar")
            system("cls")
        elif opcionMenu=="5":
            print ("\npulse una tecla para continuar")
            system("cls")
            break
        else:
            print ("")
            input("La opcion ingresada no es valida... \npulse una tecla para continuar")


vec = []
diccionario = {}
main()