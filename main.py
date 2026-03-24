from src.inventario import agregar_producto, mostrar_invenatrio,calcular_estadistica 

while True:
    print ("menu:")
    print("1-agregar un producto")
    print("2-mostrar el inventario")
    print("3-calculo de la estadistica")
    opcion = input("ingrese una opcion:")


    if opcion == "1":
            agregar_producto()
    
    if opcion == "2":
            mostrar_invenatrio()
        
    if opcion == "3":
            calcular_estadistica()
    if opcion == "4":
            print("desahabilitado")
    
    if opcion == "5":
            print("desahbilitado")
    if opcion == "6":
            print("gracias por su uso")
            break
        
                

    
        

