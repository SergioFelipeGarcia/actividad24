









lista=[10 , 'juan' , 9.95 - False , "madrid" , 15]
lista.append(' 25.95') # se añade en la ultima columna
print(lista)
#lista.sort()
for x in lista:
    print(x)
#no me salen los datos porque no puede ordenar letras con numeros


#no se puede hacer por tuple porque es inmutable


paises={'españa','rusia','Francia','China','japon'}
print(paises)#no se puede ordenar en set porque es inmutable

#7. Almacena en una colección a tu elección  los siguientes datos:
#Lunes : 7
#Martes : 8.5
#Miércoles : 6
#Jueves : 7
#Viernes : 9
#Muestra los valores por consola.
#Muestra la suma de todos
#Muestra la media de todos.
lista_dic={'Lunes':7,'Martes':8.5,'Miercoles':6,'Jueves':7,'viernes':9,}
print(lista_dic)


total=0 #totalizador
for precio in lista_dic.values():
    #total=total+precio
    total+=precio
    print(precio)
print(f'el total es {total}')
print(f'el total es {total/len(lista_dic)}')
