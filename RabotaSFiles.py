#f = open('data.txt', 'w' )
#f.write('Я налил бензин в стакан \n ')
#f.write('Стало сложно долго думать \n')
#f.close()

#with open('data.txt') as f:
#    print(f.read())
f = open('data.txt', 'r')
cont = f.read()
f.close()
words = cont.split()
print(cont)
print('В тексте {0} слов'.format(len(words)))