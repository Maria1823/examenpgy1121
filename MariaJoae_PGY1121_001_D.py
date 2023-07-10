print("""Hola, buenos dias bienvenido(a) a Creativos.cl
      Esta es la nueva plataforma de compra para el exclusivo concierto de Michael Jam""")

asist=[]
Plat=int(120000)
Gold=int(80000)
Silv=int(50000)
entradas=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100]
totp=0
totg=0
tots=0
total=0
cant=0
cantp=0
cantg=0
cants=0

while True:
    print("""ingrese la opcion que desea realizar:

    1. Comprar entradas
    2. Mostrar ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir     """)

    op=input()

    match op:
        case "1":
            cant=int(input("¿Cuantas entradas desea comprar?  (Del 1 al 3)   "))
            for i in range (cant):
                print(f""" ESCENARIO       
                {entradas}
                """)
            
            silla=input("¿que asiento desea comprar?")
            rut=input("ingrese rut de la persona a asistir:   ")
            asist.append(rut)
            asist.append(silla)
            
            if silla>0 and silla<21:
                print(f"su entrada tiene un valor de:  {Plat}")
                totp=totp+Plat 
                cantp=cantp+1
            elif silla>20 and silla<51:
                print(f"el valor de su entrada es de:  {Gold}")
                totg=totg+Gold
                cantg=cantg+1
            elif silla>50 and silla<101:
                print(f"el valor de su entrada es de:  {Silv}")
                tots=tots+Silv
                cants=cants+1
            
            
        case "2":
            print(f"""       ESCENARIO       
            {entradas}""")
          
        case "3":
            for rut in asist:
                print(rut)
                break
        case "4":
            print("""la recaudacion final es:
                  PLATINUM:   """)

        case "5":
            break

print("presione una tecla para continuar...")

    
   


