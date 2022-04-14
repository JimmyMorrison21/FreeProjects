'''
def suck(r):
    t=len(r)
    re=''
    while t > 0 :
        re += r[t - 1]
        t -= 1
    return re'''

def suck(r):
    fs = r[0]
    j = 1
    re = ''
    while j != len(r):
        re += r[j]
        j += 1
    return (re + fs)



sentence='This is my string'
arr = sentence.split(' ')
brckt=''
ch=''
for r in arr:
    if r =='!' or r =='.' or r=='?':
        ch = r
        break
    else:
        brckt += suck(r)+'ay'+' '
if ' ' == brckt[-1]:
    if ch =='':
        brckt= brckt[0:-1]

print(str(brckt+ch))
### Лучшее решение
###def pig_it(text):
###    lst = text.split()
###    return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])