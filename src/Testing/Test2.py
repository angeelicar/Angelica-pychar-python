import re
# import datetime

text = 'Esta es una de las mejores clases de testing en udemy'
search = re.search('class', text)
print (search)

if search:
    print ('que rico puerto rico')
else:
    print ('no se encontro ni chimba')