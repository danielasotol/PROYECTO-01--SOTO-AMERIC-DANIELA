
           ###### P R O Y E C T O  1 #####
           
#Análisis de la rotación de productos de LifeStore #

# Cargar listas 
from user_file import user_list
from lifestore_file import lifestore_searches, lifestore_products, lifestore_sales

#### L O G I N    D E    U S U A R I O

cond = 0

while cond == 0:
  user = input("Nombre de usuarix admin: ").lower()
  password = input("Contraseña: ").lower()

  for aux in range(len(user_list)):
    if user == user_list[aux][0] and password == user_list[aux][1]:
      print("Bienvenidx al área de administradores " + user)
      cond = 1
      admin = 1 
  if cond == 0:
    print("No existe una cuenta de administrador con estos datos.")
    client = input("Escribe 'aceptar' si deseas continuar como cliente o cualquier otra cosa para volver a intentar: ").lower()
    if client == "aceptar":
      print("Bienvenidx al área de clientes " + user)
      cond = 1
      admin = 0
    else:
      cond = 0


### A N A L I S I S   P O R   P R O D U C T O S ###

## LOS 50 PRODS MÁS Y MENOS BUSCADOS ##

# Total de búsquedas

busquedas = 0
for search in lifestore_searches:
  busquedas += 1

if admin == 1: 
  accept = input("\n Escibe 'aceptar' para ver el número de busquedas totales o cualquier otra cosa para continuar con la siguiente opción ").lower()
  if accept == "aceptar":
    print("\nNúmero de busquedas totales:" + str(busquedas))

# Pares ordenados por id y número de búsquedas

prods = []

for i in lifestore_products:
  prods.append(i[0])

searches = []
for i in prods:
    searches.append([i, 0]);


for i in lifestore_searches:
    searches[i[1]-1][1] += 1

# Los 50 ids más buscados

max_index = 0
top50br = []
searches2 = [[i for i in row] for row in searches]

for i in range(50):
  max_index = 0
  max_aux = searches2[max_index]
  for j in range(len(searches2)):
    if searches2[j][1] > max_aux[1]:
      max_index = j
      max_aux = searches2[j]
  top50br.append(max_aux)  
  if max_index == 0:
    searches2 = searches2[1:]
  else:
    searches2 = searches2[:max_index] + searches2[max_index + 1:]
top_search = top50br[1][1]

# Transformar ids a productos

for i in range(len(top50br)):
  for j in range(len(lifestore_products)):
    if top50br[i][0] == lifestore_products[j][0]:
      top50br[i][0] = lifestore_products[j][1]

# Mostrar los 50 productos más buscados y el número de búsquedas

accept = input("\n Escibe 'aceptar' para ver los 50 productos más buscados y el número de búsquedas o cualquier otra cosa para continuar con la siguiente opción ").lower()

if accept == "aceptar":

  print("\nLos 50 productos más buscados son: ")

  for i in range(len(top50br)):
    print(str(i+1) + "- " + str(top50br[i][0]) + " con " + str(top50br[i][1]) + " búsqueda(s).")

# Los 50 ids menos buscados

min_index = 0
bottom50br = []
searches3 = [[i for i in row] for row in searches]

for i in range(50):
  min_index = 0
  min_aux = searches3[min_index]
  for j in range(len(searches3)):
    if searches3[j][1] < min_aux[1]:
      min_index = j
      min_aux = searches3[j]  
  bottom50br.append(searches3[min_index])
  if min_index == 0:
    searches3 = searches3[1:]
  else:
    searches3 = searches3[:min_index] + searches3[min_index + 1:]

# Transformar ids a productos

for i in range(len(bottom50br)):
  for j in range(len(lifestore_products)):
    if bottom50br[i][0] == lifestore_products[j][0]:
      bottom50br[i][0] = lifestore_products[j][1]

# Mostrar los 50 productos menos buscados y el número de búsquedas

if admin == 1:
  accept = input("\n Escibe 'aceptar' para ver los 50 productos menos buscados y el número de búsquedas o cualquier otra cosa para continuar con la siguiente opción ").lower()
  if accept == "aceptar":
    print("\nLos 50 productos menos buscados son: ")
    for i in range(len(bottom50br)):
      print(str(i+1) + "- " + str(bottom50br[i][0]) + " con " + str(bottom50br[i][1]) + " búsqueda(s).")

## LOS 50 PRODS MÁS Y MENOS COMPRADOS ##

# Total de ventas

ventas = 0
for search in lifestore_sales:
  ventas += 1

if admin == 1:
  accept = input("\n Escibe 'aceptar' para ver el total de productos vendidos o cualquier otra cosa para continuar con la siguiente opción ").lower()
  if accept == "aceptar":
    print("\nNúmero total de productos vendidos:" + str(ventas))

# Pares ordenados por id y número de ventas

prods = []

for i in lifestore_products:
  prods.append(i[0])

sales = []
for i in prods:
    sales.append([i, 0]);


for i in lifestore_sales:
    sales[i[1]-1][1] += 1

# Los 50 ids más vendidos

top50sale = []
sales2 = [[i for i in row] for row in sales]

for i in range(50):
    max_index = 0
    max_aux = sales2[max_index]
    for j in range(len(sales2)):
        if sales2[j][1] > max_aux[1]:
            max_index = j
            max_aux = sales2[max_index]
    top50sale.append(max_aux)
    if max_index == 0:
        sales2 = sales2[1:]
    else:
        sales2 = sales2[:max_index] + sales2[max_index + 1:]

top_sale = top50sale[1][1]

# Transformar ids a productos

for i in range(len(top50sale)):
  for j in range(len(lifestore_products)):
    if top50sale[i][0] == lifestore_products[j][0]:
      top50sale[i][0] = lifestore_products[j][1]

# Mostrar los 50 productos más vendidos y el número de ventas

accept = input("\n Escibe 'aceptar' para ver los 50 productos más vendidos y el número de ventas o cualquier otra cosa para continuar con la siguiente opción ").lower()
if accept == "aceptar":
  print("\nLos 50 productos más vendidos son: ")
  for i in range(len(top50sale)):
    print(str(i+1) + "- " + str(top50sale[i][0]) + " con " + str(top50sale[i][1]) + " venta(s).")

# Los 50 ids menos vendidos

min_index = 0
bottom50sale = []
sales3 = [[i for i in row] for row in sales]

for i in range(50):
    min_index = 0
    min_aux = sales3[min_index]
    for j in range(len(sales3)):
        if sales3[j][1] < min_aux[1]:
            min_index = j
            min_aux = sales3[min_index]
    bottom50sale.append(min_aux)
    if min_index == 0:
        sales3 = sales3[1:]
    else:
        sales3 = sales3[:min_index] + sales3[min_index + 1:]

# Transformar ids a productos

for i in range(len(bottom50sale)):
  for j in range(len(lifestore_products)):
    if bottom50sale[i][0] == lifestore_products[j][0]:
      bottom50sale[i][0] = lifestore_products[i][1]

# Mostrar los 50 productos menos vendidos y el número de ventas

if admin == 1:
  accept = input("\n Escibe 'aceptar' para ver los 50 productos menos vendidos y el número de ventas o cualquier otra cosa para continuar con la siguiente opción ").lower()
  if accept == "aceptar":
    print("\nLos 50 productos menos vendidos son: ")
    for i in range(len(bottom50sale)):
     print(str(i+1) + "- " + str(bottom50sale[i][0]) + " con " + str(bottom50sale[i][1]) + " venta(s).")

### A N A L I S I S   P O R   C A T E G O R I A ###

## LAS 3 CATEGORÍAS MÁS Y MENOS BUSCADAS #

# Lista de cateogrías sin repetición

cat = []

for i in lifestore_products:
  if i[3] not in cat:
    cat.append(i[3])

# Pares de producto - cateogoría

prods = []

for i in lifestore_products:
  prods_aux = [i[0], i[3]]
  prods.append(prods_aux)

#Tercias de producto-categoría-búsquedas

search_prod = []

for i in prods:
    search_prod.append([i[0], 0, i[1]]);

for i in lifestore_searches:
    search_prod[i[1]-1][1] += 1

# Pares ordenados por cateoría y búsquedas

searches = []

for i in cat:
    searches.append([i, 0]);

for i in range(len(search_prod)):
  for j in range(len(searches)):
    if searches[j][0] == search_prod[i][2]:
      searches[j][1] += search_prod[i][1]

# Top 3 de categorías más buscadas 

max_index = 0
top3br = []
searches2 = [[i for i in row] for row in searches]

for i in range(3):
  max_index = 0
  max_aux = searches2[max_index]
  for j in range(len(searches2)):
    if searches2[j][1] > max_aux[1]:
      max_index = j
      max_aux = searches2[j]
  top3br.append(max_aux)  
  if max_index == 0:
    searches2 = searches2[1:]
  else:
    searches2 = searches2[:max_index] + searches2[max_index + 1:]
top_search = top3br[1][1]

# Mostrar las 3 categorías más buscadas y el número de búsquedas

accept = input("\n Escibe 'aceptar' para ver las 3 categorías más buscadas y el número de búsquedas o cualquier otra cosa para continuar con la siguiente opción ").lower()
if accept == "aceptar":
  print("\nLas 3 cateogrías más buscadas son: ")
  for i in range(len(top3br)):
    print(str(i+1) + "- " + str(top3br[i][0]) + " con " + str(top3br[i][1]) + " búsqueda(s).")

# Las 3 categorías menos buscadas

min_index = 0
bottom3br = []
searches2 = [[i for i in row] for row in searches]

for i in range(3):
  min_index = 0
  min_aux = searches2[min_index]
  for j in range(len(searches2)):
    if searches2[j][1] < min_aux[1]:
      min_index = j
      min_aux = searches2[j]  
  bottom3br.append(searches2[min_index])
  if min_index == 0:
    searches2 = searches2[1:]
  else:
    searches2 = searches2[:min_index] + searches2[min_index + 1:]

# Mostrar las 3 categorías menos buscadas y el número de búsquedas

if admin == 1:
  accept = input("\n Escibe 'aceptar' para ver las 3 categorías menos buscadas y el número de búsquedas o cualquier otra cosa para continuar con la siguiente opción ").lower()
  if accept == "aceptar":
    print("\nLas 3 categorías menos buscadas son: ")
    for i in range(len(bottom3br)):
      print(str(i+1) + "- " + str(bottom3br[i][0]) + " con " + str(bottom3br[i][1]) + " búsqueda(s).")


## LAS 3 CATEGORÍAS MÁS Y MENOS VENDIDAS ##

#Tercias de producto-categoría-ventas

sale_prod = []

for i in prods:
    sale_prod.append([i[0], 0, i[1]]);

for i in lifestore_sales:
    sale_prod[i[1]-1][1] += 1

# Pares ordenados por cateoría y ventas

sales = []

for i in cat:
    sales.append([i, 0]);

for i in range(len(sale_prod)):
  for j in range(len(sales)):
    if sales[j][0] == sale_prod[i][2]:
      sales[j][1] += sale_prod[i][1]

# Las 3 categorías más vendidas

top3sale = []
sales2 = [[i for i in row] for row in sales]

for i in range(3):
    max_index = 0
    max_aux = sales2[max_index]
    for j in range(len(sales2)):
        if sales2[j][1] > max_aux[1]:
            max_index = j
            max_aux = sales2[max_index]
    top3sale.append(max_aux)
    if max_index == 0:
        sales2 = sales2[1:]
    else:
        sales2 = sales2[:max_index] + sales2[max_index + 1:]

top_sale = top3sale[1][1]

# Mostrar las 3 categorías más vendidas y el número de ventas

accept = input("\n Escibe 'aceptar' para ver las 3 categorías más vendidas y el número de ventas o cualquier otra cosa para continuar con la siguiente opción ").lower()
if accept == "aceptar":
  print("\nLas 3 categorías más vendidas son: ")
  for i in range(len(top3sale)):
    print(str(i+1) + "- " + str(top3sale[i][0]) + " con " + str(top3sale[i][1]) + " venta(s).")

# Las 3 categorías menos vendidas

min_index = 0
bottom3sale = []
sales3 = sales

for i in range(3):
    min_index = 0
    min_aux = sales3[min_index]
    for j in range(len(sales3)):
        if sales3[j][1] < min_aux[1]:
            min_index = j
            min_aux = sales3[min_index]
    bottom3sale.append(min_aux)
    if min_index == 0:
        sales3 = sales3[1:]
    else:
        sales3 = sales3[:min_index] + sales3[min_index + 1:]

# Mostrar las 3 categorías menos vendidas y el número de ventas

if admin == 1:
  accept = input("\n Escibe 'aceptar' para ver las 3 categorías menos vendidas y el número de ventas o cualquier otra cosa para continuar con la siguiente opción ").lower()
  if accept == "aceptar":
    print("\nLas 3 categorías menos vendidas son: ")
    for i in range(len(bottom3sale)):
      print(str(i+1) + "- " + str(bottom3sale[i][0]) + " con " + str(bottom3sale[i][1]) + " venta(s).")

### A N A L I S I S   P O R   R E S E Ñ A ###

## LOS 20 PRODUCTOS CON MEJORES RESEÑAS ##

# Pares de compra - reseña

prods = []

for i in lifestore_sales:
  prods_aux = [i[1], i[2]]
  prods.append(prods_aux)
 

#Pares de producto - promedio de reseñas

rate_aux = []

for i in prods:
    rate_aux.append([i[0], 0, 0]);

for i in range(len(lifestore_sales)): 
  for j in range(len(rate_aux)):
    if rate_aux[j][0] == lifestore_sales[i][1]:
      rate_aux[j][1] += 1
      rate_aux[j][2] += lifestore_sales[i][2]

aux = []

for j in rate_aux:
  if j not in aux:
    aux.append(j)

rate_aux = aux 

score = []

for i in range(len(rate_aux)):  
  aux = round(rate_aux[i][2]/rate_aux[i][1], 3)
  score.append([rate_aux[i][0], aux])

aux = []

for i in lifestore_sales:
  aux.append(i[1])

for i in lifestore_products:
  if i[0] not in aux:
    score.append([i[0],0]) 

# Los 20 productos con la mejor reseña 

top20score = []
score2 = [[i for i in row] for row in score]

for i in range(20):
    max_index = 0
    max_aux = score2[max_index]
    for j in range(len(score2)):
        if score2[j][1] > max_aux[1]:
            max_index = j
            max_aux = score2[max_index]
    top20score.append(max_aux)
    if max_index == 0:
        score2 = score2[1:]
    else:
        score2 = score2[:max_index] + score2[max_index + 1:]

top_score = top20score[1][1]

# Transformar ids a productos

for i in range(len(top20score)):
  for j in range(len(lifestore_products)):
    if top20score[i][0] == lifestore_products[j][0]:
      top20score[i][0] = lifestore_products[j][1]

# Mostrar los 20 productos con mejores reseñas y la reseña promedio

accept = input("\n Escibe 'aceptar' para ver los 20 productos con mejores reseñas y la reseña promedio o cualquier otra cosa para continuar con la siguiente opción ").lower()
if accept == "aceptar":
  print("\nLos 20 productos con mejores reseñas son: ")
  for i in range(len(top20score)):
    print(str(i+1) + "- " + str(top20score[i][0]) + " con  una reseña promedio de " + str(top20score[i][1]))

## LOS 20 PRODUCTOS CON PEORES RESEÑAS ##  

# Los 20 productos con peores reseñas

min_index = 0
bottom20score = []
score3 = [[k for k in fila] for fila in score]

for i in range(20):
    min_index = 0
    min_aux = score3[min_index]
    for j in range(len(score3)):
        if score3[j][1] < min_aux[1]:
            min_index = j
            min_aux = score3[min_index]
    bottom20score.append(min_aux)
    if min_index == 0:
        score3 = score3[1:]
    else:
        score3 = score3[:min_index] + score3[min_index + 1:]

# Transformar ids a productos

for i in range(len(bottom20score)):
  for j in range(len(lifestore_products)):
    if bottom20score[i][0] == lifestore_products[j][0]:
      bottom20score[i][0] = lifestore_products[i][1]

# Mostrar los 20 productos con peores reseñas y el promedio

if admin == 1:
  accept = input("\n Escibe 'aceptar' para ver los 20 productos con peores reseñas y el promedio o cualquier otra cosa para continuar con la siguiente opción ").lower()
  if accept == "aceptar":
    print("\nLos 20 productos con peores reseñas son: ")
    for i in range(len(bottom20score)):
      print(str(i+1) + "- " + str(bottom20score[i][0]) + " con " + " con  una reseña promedio de " +str(bottom20score[i][1]))

### A N A L I S I S   I N G R E S O - V E N T A ###

## INGRESOS Y VENTAS ANUALES ##

# Generar sublistas con  producto - precio - mes - año

sales_date = []

for i in range(len(lifestore_sales)):
 for j in  range(len(lifestore_products)):
   if lifestore_sales[i][1] == lifestore_products[j][0]:
    sales_date.append([lifestore_sales[i][1], lifestore_products[j][2], lifestore_sales[i][3][3:5], lifestore_sales[i][3][6:10]])

# Lista de años sin repetición

year = []

for i in sales_date:
  if i[3] not in year:
    year.append(i[3])

# Tercias ordenadas de años - ventas - ingresos

sales_y = []

for i in year:
    sales_y.append([i, 0, 0]);

for i in sales_date:
  for j in sales_y:
    if  j[0] ==  i[3]:
      j[1] += 1
      j[2] += i[1]

# Mostrar las ventas y los ingresos por año:

if admin == 1:
  accept = input("\n Escibe 'aceptar' para ver las ventas y los ingresos por año o cualquier otra cosa para continuar con la siguiente opción ").lower()
  if accept == "aceptar":  
    for i in range(len(sales_y)):
     print(str(i+1) + "- La venta en " + str(sales_y[i][0]) + " fue de " + str(sales_y[i][1]) + " producto(s) con  un valor de " + str(sales_y[i][2]) + " pesos. ")

 ## INGRESOS Y VENTAS MENSUALES PROMEDIO ##

avg_sale = round(sales_y[0][1]/12,3)
avg_income = round(sales_y[0][2]/12,3)

if admin == 1:
  accept = input("\n Escibe 'aceptar' para ver el promedio mensual de ventas e ingresos o cualquier otra cosa para continuar con la siguiente opción ").lower()
  if accept == "aceptar":  
    print("\nDurante el " + str(sales_y[0][0]) +" el promedio mensual de ventas fue de " + str(avg_sale) + " artículos. El ingreso promedio mensual fue de " + str(avg_income) + " pesos ")

## INGRESOS Y VENTAS MENSUALES ##

# Lista de meses sin repetición

month = []

for i in sales_date:
  if i[2] not in month:
    month.append(i[2])

# Tercias ordenadas de mes - ventas - ingresos

sales_m = []

for i in month:
  for j in year:
    if j == '2020':
      sales_m.append([i, 0, 0]);

for i in sales_date:
  for j in sales_m:
    if  j[0] ==  i[2]:
      j[1] += 1
      j[2] += i[1]

# Los 5 meses con las mayores ventas 

top5sale = []
sales_m2 = [[i for i in row] for row in sales_m]
for i in range(5):
    max_index = 0
    max_aux = sales_m2[max_index]
    for j in range(len(sales_m2)):
        if sales_m2[j][1] > max_aux[1]: 
            max_index = j
            max_aux = sales_m2[max_index]
    top5sale.append(max_aux)
    if max_index == 0:
        sales_m2 = sales_m2[1:]
    else:
        sales_m2 = sales_m2[:max_index] + sales_m2[max_index + 1:]

top_sale = top5sale[1][1]

# Transformar ids a productos

for i in range(len(top5sale)):
  for j in range(len(lifestore_products)):
    if top5sale[i][0] == lifestore_products[j][0]:
      top5sale[i][0] = lifestore_products[j][1]

# Mostrar los 5 meses con mayores ventas

if admin == 1:
  accept = input("\n Escibe 'aceptar' para ver los 5 meses con mayores ventas o cualquier otra cosa para continuar con la siguiente opción ").lower()
  if accept == "aceptar":  
    print("\nLos 5 meses con mayores ventas fueron: ")
    for i in range(len(top5sale)):
      print(str(i+1) + "- " + str(top5sale[i][0]) + " con una venta de " + str(top5sale[i][1]) + " artículos. ") 

# Los 5 meses con las mayores ingresos

top5income = []
sales_m2 = [[i for i in row] for row in sales_m]

for i in range(5):
    max_index = 0
    max_aux = sales_m2[max_index]
    for j in range(len(sales_m2)):
        if sales_m2[j][2] > max_aux[2]:
            max_index = j
            max_aux = sales_m2[max_index]
    top5income.append(max_aux)
    if max_index == 0:
        sales_m2 = sales_m2[1:]
    else:
        sales_m2 = sales_m2[:max_index] + sales_m2[max_index + 1:]

top_income = top5income[1][1]

# Transformar ids a productos

for i in range(len(top5income)):
  for j in range(len(lifestore_products)):
    if top5income[i][0] == lifestore_products[j][0]:
      top5income[i][0] = lifestore_products[j][1]

# Mostrar los 5 meses con mayores ingresos

if admin == 1:
  accept = input("\n Escibe 'aceptar' para ver los 5 meses con mayores ingresos o cualquier otra cosa para continuar con la siguiente opción ").lower()
  if accept == "aceptar":  
    print("\nLos 5 meses con mayores ingresos fueron: ")
    for i in range(len(top5income)):
      print(str(i+1) + "- " + str(top5income[i][0]) + " con total de " + str(top5income[i][2]) + " pesos. ")

print("\n ¡Gracias por tu preferencia!")