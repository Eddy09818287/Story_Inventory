#definir variables:
i=0
nombre_producto = input("ingrese nombre del producto:")
#pedir precio con validacion
while True:
    try:
        precio_producto = float(input("ingrese precio del producto:"))
        if i > precio_producto:
            print("ingrese un valor numerico correcto")
            continue
        break
    except ValueError:
        print("ingrese solo numeros :")
#pedir la cantidad de producto con validacion
while True:
    try:
        cantidad_producto = int(input("ingrese la cantidad de su producto:"))
        if i> cantidad_producto :
            print("ingrese un valor numerico correctro ")
            print("ingrese un valor correcto:")
            continue
        break
    except ValueError:
       print("ingrese un valor correcto:")
while True:
  costo_total = precio_producto * cantidad_producto
  print(f"su producto es:{nombre_producto}")
  print(f"el precio de su producto es ¿:{precio_producto}")
  print(f"la cantidad que llevara es de:{cantidad_producto}")
  print(f"su total a pagar es de {costo_total}")
  break




