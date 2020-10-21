import re
import time
try:
    f= open("ejemplo.txt").read()
except:
    exit()
    print ("Error")
def expresion(patron):
    busqueda= re.findall(patron,f,flags=re.MULTILINE)
    print("Palabras encontradas "+str(busqueda))
    print("Numero de Coincidencias "+str(len(busqueda)))
def imprimir():
    print("-------------------------------")
    print("Expresiones Regulares en Python")
    print("-------------------------------")
    print()
    print("Opciones disponibles:")
    print("1. Todas las palabras que tengan una longitud de 7 o más letras")
    print("2. Expresiones que NO finalicen con una vocal")
    print("3. Las palabras que inicien con “M” donde la segunda letra no sea vocal")
    print("4. Expresiones encerradas entre comillas")
    print("5. Ip’s")
    print("6. Horas")
    print("7. Teléfonos")
    print("8. Correos electrónicos")
    print("9. Url’s")
    print("10. Codigo Postal")
    print("0. Salir")
    print()
def menu():
    while True:
        imprimir()
        try:
            entrada_usuario = int(input("Seleccione una opcion: "))
            if entrada_usuario in range(11):
                if entrada_usuario == 0:
                    print("Adios! Vuelva pronto")
                    break
                    print()
#---------------------------------------------------------------------------------------------------------------------------------------------
                elif entrada_usuario == 1:
                    print("Todas las palabras que tengan una longitud de 7 o más letras") 
                    patron = "[a-zA-Z]{7,}"
                    expresion(patron)
                    print("Espere 3 segundos para volver a mostrar el menu") 
                    time.sleep(3)
#---------------------------------------------------------------------------------------------------------------------------------------------
                elif entrada_usuario == 2:
                    print("Expresiones que NO finalicen con una vocal") 
                    patron = "[a-zA-Z]+[^aeiou]\s"
                    expresion(patron)
                    print("Espere 3 segundos para volver a mostrar el menu") 
                    time.sleep(3)
#---------------------------------------------------------------------------------------------------------------------------------------------
                elif entrada_usuario == 3:
                    print("Las palabras que inicien con “M” donde la segunda letra no sea vocal") 
                    patron = "M[^aeiou][a-zA-Z]{1,}"
                    expresion(patron)
                    print("Espere 3 segundos para volver a mostrar el menu") 
                    time.sleep(3)
#---------------------------------------------------------------------------------------------------------------------------------------------
                elif entrada_usuario == 4:
                    print("Expresiones encerradas entre comillas") 
                    patron = "\".*?\"|\'.*?\'"
                    expresion(patron)
                    print("Espere 3 segundos para volver a mostrar el menu") 
                    time.sleep(3)
#---------------------------------------------------------------------------------------------------------------------------------------------
                elif entrada_usuario == 5:
                    print("Ip’s") 
                    patron = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^0-9]"
                    expresion(patron)
                    print("Espere 3 segundos para volver a mostrar el menu") 
                    time.sleep(3)
#---------------------------------------------------------------------------------------------------------------------------------------------
                elif entrada_usuario == 6:
                    print("Horas") 
                    patron = "(?:[01]\d|2[0-3]):[0-5]\d"
                    expresion(patron)
                    print("Espere 3 segundos para volver a mostrar el menu") 
                    time.sleep(3)
#---------------------------------------------------------------------------------------------------------------------------------------------
                elif entrada_usuario == 7:
                    print("Teléfonos") 
                    patron = "(\d{3}[\s-]\d{3}[\s-]\d{4})|(\d[0-9]{7,10})"
                    expresion(patron)
                    print("Espere 3 segundos para volver a mostrar el menu") 
                    time.sleep(3)
#---------------------------------------------------------------------------------------------------------------------------------------------
                elif entrada_usuario == 8:
                    print("Correos electrónicos") 
                    patron = "[a-zA-Z0-9.!#$%&'*+=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*"
                    expresion(patron)
                    print("Espere 3 segundos para volver a mostrar el menu") 
                    time.sleep(3)
#---------------------------------------------------------------------------------------------------------------------------------------------
                elif entrada_usuario == 9:
                    print("Url’s") 
                    patron = "https?:\/\/[\w\-]+\.[\w\-]+[#?]?.*"
                    expresion(patron)
                    print("Espere 3 segundos para volver a mostrar el menu") 
                    time.sleep(3)
#---------------------------------------------------------------------------------------------------------------------------------------------
                elif entrada_usuario == 10:
                    print("Codigo Postal") 
                    patron = "^(\d{5}$)"
                    expresion(patron)
                    print("Espere 3 segundos para volver a mostrar el menu") 
                    time.sleep(3)
#---------------------------------------------------------------------------------------------------------------------------------------------
            else:
                print('Error, solo de aceptan numeros del 0 al 11')
        except ValueError:
            print("Error, ingrese solamente numeros")
if __name__ == '__main__':
    menu()