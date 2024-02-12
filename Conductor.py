
nombres = []
kms = []

total_kms=[]
num = int(input("ingresar el # de coductores"))   
for _ in range(num):  
        nombre_conductor = input("Ingrese el nombre del conductor: ")
        nombres.append(nombre_conductor)

        kmscon = []
        for dia in range(7):
            kms_dia = float(input(f"Ingrese los kilómetros conducidos por {nombre_conductor} el día {dia + 1}: "))
            kmscon.append(kms_dia)

        kms.append(kmscon)
        total_kms.append(sum(kmscon)) 

   
print("\nTotal de kilómetros conducidos por cada conductor:")
for nombre, total_kms in zip(nombres, total_kms):
        print(f"{nombre}: {total_kms} km")

