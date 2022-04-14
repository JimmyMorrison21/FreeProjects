from itertools import *
r=''
brckt=[]
for i in permutations('aabb'):
    for k in i :
        r += k
        if len(r) == len('aabb'):
            brckt.append(r)
            r = ''
print(list(set(brckt)))
''' НАПИСАЛ ПРАВИЛЬНО , КОДВАРС ГОВНО ЗАШАКАЛИЛИ НАЗВАНИЕ ФУНКЦИИ 
    НИЖЕ КОД ДЛЯ НАПИСАННЫЙ ФАРШМАКОМ 
    
def permutations(string):
    result = set([string])
    if len(string) == 2:
        result.add(string[1] + string[0])

    elif len(string) > 2:
        for i, c in enumerate(string):                            #### ENUMERATE ТОП ТЕМА ВЫВОДИТ НОМЕР ПРОХОДА И ЭЛЕМЕНТ СПИСКА
            for s in permutations(string[:i] + string[i + 1:]):
                result.add(c + s)

    return list(result)




'''

