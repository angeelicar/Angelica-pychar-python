# imprimir
Nombre = 'Angelica Niño'
print('Hola', Nombre, 'eres hermosa')

# arregloslista
List = ['Venezuela', 'Chile', 'Peru', 'transilvania']
for paises in List:
    if paises == 'transilvania':
        print('que loco')
    else:
        print('que triste')
for paises in List:
    print(paises)
    if paises == 'Chile':
        print(Nombre, 'vive en', paises, 'pero no le gusta')
        continue
chuchi = 0
for paises in List:
    if paises == 'Venezuela':
        chuchi = chuchi+3
        print(chuchi)
    if paises == 'Chile':
        chuchi = chuchi+2
        print(chuchi)
    if paises == 'Peru':
        chuchi = chuchi+7
        print(chuchi)

# diccionario
diccionario = {'Nombre': 'Angelica', 'Edad': '26', 'Hijos': 'Lucia'}
Nombredic = diccionario['Nombre']
Edaddic = diccionario['Edad']
Hijosdic = diccionario['Hijos']
print(Nombredic)
print(Edaddic)
print(Hijosdic)
diccionario['Nombre']= 'Edgar Alejandro Quintero'
print(diccionario['Nombre'])
print(diccionario)