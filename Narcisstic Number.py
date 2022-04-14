g = 153
s = str(g)
dl=len(s)
z=0
for i in s:
    z += int(i)**dl
print(z)
if z == g:
    f = True
else:
    f = False
print(f)