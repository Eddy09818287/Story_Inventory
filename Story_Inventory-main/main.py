from src.inventario import agregar_producto, mostrar_invenatrio,calcular_estadistica, quitar_producto, actualizar_productos,buscar_producto

while True:
    print ("------MENU------")
    print("1-agregar un producto")
    print("2-mostrar el inventario")
    print("3-calculo de la estadistica")
    print("4-quitar un producto")
    print("5-actualizar un producto")
    print("6-buscar un producto")
    opcion = input("ingrese una opcion:")


    if opcion == "1":
            agregar_producto()
    
    if opcion == "2":
            mostrar_invenatrio()
        
    if opcion == "3":
            calcular_estadistica()
    if opcion == "4":
            quitar_producto()
    
    if opcion == "5":
           actualizar_productos()
          
    if opcion == "6":
            buscar_producto()

    

    
            