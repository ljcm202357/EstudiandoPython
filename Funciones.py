#funcion sin parametros sin retorno
def inicio():

    print("MENU PRINCIPAL")
    print("Seleccione la opcion  correcta:")
    print("1. Operacion sumar")
    print("2 Operacion resta")
    print("3 Operacion Multiplicar")
    print("4 Operacion Dividir")
    print("5 Salir ")

def main():
    while True:
        inicio()
        opcion = int(input("Seleccione la opcion"))
        if opcion == 1:    
            print("Ha seleccionado la suma ")
            Num1 = int(input("Ingresar el 1 numero"))
            Num2 = int(input("Ingresar el 2 numero"))
            Sumar = Num1+Num2
            print("EL resultado de la suma es: ",Sumar)
        elif opcion == 2:
            print("Ha seleccionado operacion resta")
            Num1 = int(input("Ingresar el 1 numero"))
            Num2 = int(input("Ingresar el 2 numero"))
            Restar = Num1-Num2
            print("EL resultado de la resta es: ",Restar)
        elif opcion == 3:
             print("Ha seleccionado operacion multiplicar")
        elif opcion == 4:
              print("Ha seleccionado operacion dividir")  
        elif opcion == 5:
             print("Hasta luego")  
             break    
        else:
             print("Opcion no valida, seleccione una opcion valida")                

main()   
