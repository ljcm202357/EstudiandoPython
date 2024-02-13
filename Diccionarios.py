Persona = {
    "Nombre":"Leidy Johanna",
    "Apellido":"Cifuentes Martinez",
    "Estatura":1.59,
    "Edad":50,
    "Email":"cifuentes0903@gmail.com",
    "CiudadNac":"Ibague",
    "Genero":["Femenino","Masculino","Otro"]

}
print(Persona)
#mostrar un elemento del diccionario
print("El nombre de la persona es:", {Persona["Nombre"]})
#agregar elemento del diccionario
Persona["Telefono"]=315851935
print(Persona)
#Modificar valor del elemento del diccinario
Persona["Telefono"]=2669032
print(Persona)
#Modificar la clave del elemento 
Persona["Celular"] = Persona.pop("Telefono")
print(Persona)
#Eliminar un elemento del diccionario
del Persona["Celular"]
print(Persona)

#Iterar los item de las claves y valores
for clave,valor in Persona.items():
    print(clave , ": " , valor)