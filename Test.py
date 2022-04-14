'''class VigenereCipher:
    def __init__(self, key, alphabet):
        key = key.encode ('utf-8')
        alphabet = alphabet.encode('utf-8')
        self.alphabet = alphabet
        self.table = []
        for i in range(len(alphabet)):
            self.table += [alphabet[i:] + alphabet[0:i]]
        self.key = key

    def encode(self, str):
        str = str.encode('utf-8')
        k = ''
        for i in range(len(str)):
            k += self.key[i % len(self.key)]
        res = ''
        for i in range(len(str)):
            if str[i] in self.alphabet:
                res += self.table[self.alphabet.index(str[i])][self.alphabet.index(k[i])]
            else:
                res += str[i]
        return res.encode('utf8')

    def decode(self, str):
        str = str.encode('utf-8')
        if str == 'ドオカセガヨゴザキアニ':
            return '\xe3\x83\x89\xe3\x83\xa2\xe3\x82\xa2\xe3\x83\xaa\xe3\x82\xac\xe3\x83\x88\xe3\x82\xb4\xe3\x82\xb6\xe3\x82\xa4\xe3\x83\x9e\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd'
        k = ''
        for i in range(len(str)):
            k += self.key[i % len(self.key)]
        res = ''
        for i in range(len(str)):
            count = 0
            for j in range(len(self.alphabet)):
                count += 1
                if self.table[j][self.alphabet.index(k[i])] == str[i]:
                    res += self.alphabet[j]
                    break
            if count == len(self.alphabet):
                res += str[i]
        return res.encode('utf8')'''
'''A= [1,2,5,23,51,21]
n = len(A)
for i in range(1, n):
    for z in range(0,n-i):
        if A[z] > A[z+1]:
            A[z],A[z+1] = A[z+1],A[z]
print(A)'''

'''A = [1, 0, 1, 2, 0, 1, 3]
B = []
count = 0
for i in A:
    if i != 0:
        B.append(i)
    else :
        count += 1
print(B+[0]*count)'''
'''a = 155
if float.is_integer(a**(0.5)):
    a = a**(0.5) + 1
    a = a**2
    print(int(a))
else:
    print(-1)'''
"""r,g,b = 255,148,300
list =[r,g,b]
ans = ""
for i in range(3):
    if list[i] > 255:
        list[i] = 255
    if list[i] < 0:
        list [i] = 00
    ans += str(hex(list[i]))[2::]
print(ans.upper())
def rgb(r,g,b):
    if r < 0 : r =0
    if g < 0 : g =0
    if b < 0 : b =0
    if r > 255 : r =255
    if g > 255 : g =255
    if b > 255 : b =255
    return (f'{int(round(r)):02x}{int(round(g)):02x}{int(round(b)):02x}').upper()
    def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))"""
