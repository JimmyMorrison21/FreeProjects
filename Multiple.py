kort={0,1}
n= '1df1'
brckt=[]
r=len(n)
res=0
for i in n :
    if i in kort:
        res += int(i) * 2 ** (r)
        r -= 1
        print("hello")
    else:
        break
        print("net")