s = [1, 1, 1, 1]
count = len(s)
z = 0
for i in s :
    z += (i * 2**(count))/2
    count -= 1
print(int(z))