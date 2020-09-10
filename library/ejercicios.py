
def agregar(vec,diccionario):
    diccionario = {}

    diccionario ['id'] = input("Ingresa el id del funcionario >> ")
    diccionario ['Nombre'] = input("Ingresa el nombre del funcionario >> ")
    diccionario ['Cargo'] = input("Ingresa el cargo del funcionario >> ")
    diccionario ['Salario'] = input("Ingresa el salario del funcionario >> ")
    
    vec.append(diccionario)


def mostrar(vec,diccionario):

    print ("-----------------------------------------------------------------------")
    for dic in vec:
        for llave in dic:
            print(f'{llave} : {dic[llave]}')
        print ("-----------------------------------------------------------------------")


