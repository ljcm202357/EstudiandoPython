#definir las listas
Nombres=[]
Notas=[]
Amejor =[]
mb=0
b=0
iN=0
#LLenar la lista
for x in range(1,5):
    Nom = input(f"Por favor ingresar el nombre del alumno {x} : ")
    Nombres.append(Nom)
    No = int(input(f"Por favor ingresar las notas del alumnos {x} : "))
    Notas.append(No)
#recorrer la lista
for y in range(len(Nombres)):
    print(f"El alumno(A){Nombres[y]}",f"Tiene la nota {Notas[y]}")
      

    if Notas[y]>=8:
        print("Alumno muy bueno")
        mb += 1
        Amejor.append(Nombres[y])
    else:
        if Notas[y]>=4:
            print("Alumno bueno")
            b += 1
        else:
            print("Alumno no aprueba la materia")
            iN += 1
print("Listado inicial de los alumnos son : ",Nombres)              
#Mostrar solo los alumnos que son alumnos bueno
eliminar = []            
for z in range(len(Notas)):
    if 4 <= Notas[z] <= 7:
        ##Notas.pop(z)
        ##Nombres.pop(z)   
        eliminar.append(z)
for d in sorted(eliminar,reverse=True):
    Notas.pop(d)
    Nombres.pop(d)

print("Cantidad de alumnos muy buenos son: ",mb)   
      
print("Lo nombres de los mejores alumnos x nota son: ",Amejor)
print("Listado de alumnos ",Nombres)
