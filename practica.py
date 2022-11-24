from cliente import Cliente

print('practica de colecciones')
#crear una lista de frutas con 14 frutas
#muestra las frutas ordenadas alfavetico
lista=['fresa','manzana','pera','mango','platano','kiwi','sandia','piña','coco']
lista.append('macedonia')

print(lista)
lista.sort()
for x in lista:
    print(x)

#añade a las fruta macedonia
lista.append('macedonia')
#crea un diccionario nuevo con las frutas y los precios
import statistics as stats
lista_dic={'fresa':12.3,'pera':4.5}
print(lista_dic)
#mostrar precio medio

total=0 #totalizador
for precio in lista_dic.values():
    total=total+precio
    print(precio)
print(f'el total es {total}')

total=0 #totalizador
for precio in lista_dic.values():
    #total=total+precio
    total+=precio
    print(precio)
print(f'el total es {total}')
print(f'el total es {total/len(lista_dic)}')



#guardar 4 paises del mundo.No se pueden añadir mas paises.los quiero ordenar alfabeticamente
paises=['españa','francia','china','estados unidos']

paises.sort()
for x in paises:
    print(x)
# 3 alumnos con sus notas : decimales
#muestra  unicamente los alumnos cuya nota es superior o  igual a 5

notas={'Paco':7.2,'Emi':5,'Sandra':3}

for nota in notas.items():
    if nota[1]>=5:
        print(nota[0])
cliente1=Cliente('juan''madrid',1500)#instanciar una clase
cliente2=Cliente('paula''madrid',1500)#instanciar una clase
cliente3=Cliente('javier','madrid',1500)#instanciar una clase
clientes=[cliente1,cliente2,cliente3]
