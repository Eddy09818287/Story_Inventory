inventario = []
def agregar_producto():
    nombre_producto = input("ingrese nombre del producto:")
# pedir precio con validacion
    i = 0
    while True:
        try:
            precio_producto = float(input("ingrese precio del producto:"))
            if i > precio_producto:
                print("ingrese un valor numerico correcto")
                continue
            break
        except ValueError:
            print("ingrese solo numeros :")
    # pedir la cantidad de producto con validacion
    while True:
        try:
            cantidad_producto = int(input("ingrese la cantidad de su producto:"))
            if i > cantidad_producto:
                print("ingrese un valor numerico correctro ")
                print("ingrese un valor correcto:")
                continue
            break
        except ValueError:
            print("ingrese un valor correcto:")

    
    producto = {
      "nombre" : nombre_producto,
      "precio": precio_producto,
      "cantidad": cantidad_producto,
    }
    inventario.append(producto)
    print("producto agregado correctamente")

    
def mostrar_invenatrio():
    print("---INVENTARIO---")
    if len (inventario) == 0:
        print("inventario esta vacio")
    else:
        for producto in inventario:
            print (f"producto:{producto['nombre']} | precio:{producto['precio']} | cantidad:{producto['cantidad']}" )
            



                

    





